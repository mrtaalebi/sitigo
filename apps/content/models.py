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
    image_temp.save(output_io_stream, format='JPEG', quality=100)
    output_io_stream.seek(0)
    img = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % img.name.split('.')[0],
                               'image/jpeg', sys.getsizeof(output_io_stream), None)
    return img


class Post(models.Model):
    content = RichTextField()


class ImageUpload(models.Model):
    caption = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.image = resize(self.image, 500, 400)
        super(ImageUpload, self).save(*args, **kwargs)


class FileUpload(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField()
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            if self.image:
                self.image = resize(self.image, 200, 200)
        super(FileUpload, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Age(models.Model):
    persian_name = models.CharField(max_length=400, default='a')  # todo ino bardar
    english_name = models.CharField(max_length=400, default='a')
    poster = models.ImageField()
    files = models.ManyToManyField(FileUpload)
    persian_content = RichTextField()
    english_content = RichTextField()
    year = models.IntegerField()
    images = models.ManyToManyField(ImageUpload)

    def __str__(self):
        return self.english_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.poster = resize(self.poster, 1000, 1500)
        super(Age, self).save(*args, **kwargs)


class Category(models.Model):
    LANG_CHOICES = (
        ('fa', _('persian')),
        ('en', _('english'))
    )
    language = models.CharField(choices=LANG_CHOICES, max_length=128, default='fa')
    name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.ForeignKey(FileUpload, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
