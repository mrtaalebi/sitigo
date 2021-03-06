from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils.translation import ugettext_lazy as _


def resize(img, x, y):
    image_temp = Image.open(img)
    output_io_stream = BytesIO()
    image_temp = image_temp.resize((x, y))
    image_temp.save(output_io_stream, format='PNG', quality=100)
    output_io_stream.seek(0)
    img = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % img.name.split('.')[0],
                               'image/jpeg', sys.getsizeof(output_io_stream), None)
    return img


class FileUpload(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)
    file = models.FileField(null=False, blank=False)
    thumbnail = models.ImageField(null=True, blank=True)
    language = models.CharField(
            choices=(
                ('fa', _('fa')),
                ('en', _('en')),
                ('all',_('all'))
                ),
            default='all',
            max_length=200
        )

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            self.thumbnail = self.make_preview(self.file)
        if self.thumbnail:
            self.thumbnail = resize(self.thumbnail, 500, 500)
        
        if not self.name:
            self.name = self.file.name

        super(FileUpload, self).save(*args, **kwargs)

    def make_preview(self, file):
        print(file)
        import subprocess
        from django.conf import settings
        import os
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile


        thumb_name = 'T_' + file.name + '.png'
        thumb_path = os.path.join(settings.MEDIA_ROOT, thumb_name)
        
        path = default_storage.save('tmp/' + file.name, ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        params = ['convert', tmp_file + "[0]", thumb_path]

        result = subprocess.call(params)
        print("result {}".format(result))
        if result != 0:
            thumb_name = 'default_thumbnail.png'

        return thumb_name
        

    def __str__(self):
        return '/content/download?file={}'.format(self.file.name)


class Event(models.Model):
    persian_name = models.CharField(max_length=400, default='a')  # todo ino bardar
    english_name = models.CharField(max_length=400, default='a')
    poster = models.ImageField()
    english_poster = models.ImageField(null=True)
    files = models.ManyToManyField(FileUpload)
    persian_content = RichTextField()
    english_content = RichTextField()
    year = models.IntegerField()

    def __str__(self):
        return self.english_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.poster = resize(self.poster, 1000, 1500)
            if self.english_poster == None:
                self.english_poster = self.poster
        super(Event, self).save(*args, **kwargs)


class Category(models.Model):
    LANG_CHOICES = (
        ('fa', _('persian')),
        ('en', _('english'))
    )
    language = models.CharField(choices=LANG_CHOICES, max_length=128, default='fa')
    name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)

    def __str__(self):
        return str(self.cat) + ' - ' + self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)

    file = models.ForeignKey(FileUpload, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
