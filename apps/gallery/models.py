from django.db import models
from PIL import Image as PIL_Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from apps.content.models import Event


def resize(img, max_height, x_to_y):
    image_temp = PIL_Image.open(img)
    output_io_stream = BytesIO()
    y = int(max_height if image_temp.size[1] > max_height else image_temp.size[1])
    x = int(y * image_temp.size[0] / image_temp.size[1])
    image_temp = image_temp.resize((x, y))
    if image_temp.size[0] / image_temp.size[1] - x_to_y > 1e-5:
        image_temp = image_temp.crop((
                int((image_temp.size[0] - image_temp.size[1] * x_to_y) / 2),
                0,
                int(image_temp.size[0] - (image_temp.size[0] - image_temp.size[1] * x_to_y) / 2),
                image_temp.size[1])
            )
    image_temp.save(output_io_stream, format='PNG', quality=100)
    output_io_stream.seek(0)
    img = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % img.name.split('.')[0],
                               'image/jpeg', sys.getsizeof(output_io_stream), None)
    return img


class Image(models.Model):
    persian_caption = models.CharField(max_length=200, null=True, blank=True, default="default")
    english_caption = models.CharField(max_length=200, null=True, blank=True, default="default")
    country_event = models.ForeignKey('CountryEvent', on_delete=models.CASCADE)
    city = models.ForeignKey('City', null=True, blank=True, on_delete=models.CASCADE)

    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.image = resize(self.image, 1000, 1e10)
            if self.city is not None:
                location_persian = self.country_event.country.persian_name + " - " + self.city.persian_name
                location_english = self.country_event.country.english_name + " - " + self.city.english_name
            else:
                location_persian = self.country_event.country.persian_name
                location_english = self.country_event.country.english_name

            if self.persian_caption == "default":
                self.persian_caption = self.country_event.event.persian_name.split()[0] + " المپیاد هندسه در " \
                        + location_persian
            if self.english_caption == "default":
                self.english_caption = self.country_event.event.english_name.split()[0] + " IGO in " \
                        + location_english
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.english_caption) + ' - ' + str(self.country_event)


class CountryEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.event) + ' - ' + str(self.country)


class Country(models.Model):
    persian_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)

    def __str__(self):
        return self.english_name


class City(models.Model):
    persian_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)

    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.english_name


class Gallery(models.Model):
    persian_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.english_name


class GroupImageUpload(models.Model):
    country_event = models.ForeignKey(CountryEvent, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    zip_file = models.FileField(upload_to='group_image_upload/')

    persian_caption = models.CharField(max_length=300, default='default', blank=True)
    english_caption = models.CharField(max_length=300, default='default', blank=True)

    images = models.ManyToManyField(Image, related_name='group_upload', blank=True, null=True)

    re_upload = models.BooleanField(default=False)

    def create_images(self):

        import os
        unzip_path = os.path.abspath(
                os.path.join(
                    os.path.join(
                        settings.MEDIA_ROOT,
                        'group_image_upload_unzip'),
                    self.zip_file.name.split('.')[0]
                )
            )
        import subprocess
        params = ['mkdir', '-p', unzip_path]
        subprocess.call(params)
        params = [
                'unzip',
                '-j',
                '-o',
                str(self.zip_file.file),
                '-d',
                unzip_path
            ]
        subprocess.call(params)

        imgs = os.listdir(unzip_path)
        for img in imgs:
            self.images.add(
                Image.objects.create(
                    country_event=self.country_event,
                    city=self.city,
                    persian_caption=self.persian_caption,
                    english_caption=self.english_caption,
                    image=os.path.join(unzip_path, img)
                )
            )

    def save(self, *args, **kwargs):
        super(GroupImageUpload, self).save(*args, **kwargs)

        if self.re_upload or self.images.all().count() == 0:
            Image.objects.filter(group_upload=self).delete()
            import threading
            threading.Thread(target=self.create_images).start()
        self.re_upload = False
        super(GroupImageUpload, self).save(*args, **kwargs)

    def delete(self):
        Image.objects.filter(group_upload=self).delete()
        super().delete()

    def __str__(self):
        return str(self.country_event) + " - " + str(self.city) + " - " + str(self.zip_file.name)

