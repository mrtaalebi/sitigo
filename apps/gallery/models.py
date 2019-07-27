from django.db import models
from PIL import Image as PIL_Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils.translation import ugettext_lazy as _

from apps.content.models import Event


def resize(img, x, y):
    image_temp = PIL_Image.open(img)
    output_io_stream = BytesIO()
    image_temp = image_temp.resize((x, y))
    image_temp.save(output_io_stream, format='PNG', quality=100)
    output_io_stream.seek(0)
    img = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % img.name.split('.')[0],
                               'image/jpeg', sys.getsizeof(output_io_stream), None)
    return img


class Image(models.Model):
    persian_caption = models.CharField(max_length=100, null=True, blank=True)
    english_caption = models.CharField(max_length=100, null=True, blank=True)
    country_event = models.ForeignKey('CountryEvent', on_delete=models.CASCADE)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.image = resize(self.image, 800, 600)
            if self.persian_caption == "":
                self.persian_caption = self.country_event.event.persian_name + " در " \
                        + self.country_event.country.persian_name
            if self.english_caption == "":
                self.english_caption = self.country_event.event.english_name + " in " \
                        + self.country_event.country.english_name
        super(Image, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.english_caption) + ' - ' + str(self.country_event)


class CountryEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event) + ' - ' + str(self.country)


class Country(models.Model):
    persian_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)

    def __str__(self):
        return self.english_name

