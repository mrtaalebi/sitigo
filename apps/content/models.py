from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Post(models.Model):
    content = RichTextField()


class FileUpload(models.Model):
    name = models.CharField(max_length=50)
    file = RichTextUploadingField()
    image = models.ImageField(null=True)


class Age(models.Model):
    poster = models.ImageField()
    files = models.ManyToManyField(FileUpload)
    content = RichTextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.poster = self.resize_poster(self.poster)
        super(Age, self).save(*args, **kwargs)

    def resize_poster(self, img):
        image_temp = Image.open(img)
        output_io_stream = BytesIO()
        image_temp = image_temp.resize((1000, 1500))
        image_temp.save(output_io_stream, format='JPEG', quality=100)
        output_io_stream.seek(0)
        img = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % img.name.split('.')[0],
                                   'image/jpeg', sys.getsizeof(output_io_stream), None)
        return img