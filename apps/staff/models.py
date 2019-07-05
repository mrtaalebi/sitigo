from django.db import models
import sys
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

# Create your models here.
from apps.content.models import Age


class Role(models.Model):
    persian_name = models.CharField(max_length=300)
    english_name = models.CharField(max_length=300)


class Staff(models.Model):
    event = models.ForeignKey(Age, on_delete=models.CASCADE)
    persian_name = models.CharField(max_length=300)
    english_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='staff_photos')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.image = self.resize(self.image)
        super(Staff, self).save(*args, **kwargs)

    def resize(self, img):
        image_temp = Image.open(img)
        output_io_stream = BytesIO()
        image_temp = image_temp.resize((200, 200))
        image_temp.save(output_io_stream, format='JPEG', quality=100)
        output_io_stream.seek(0)
        img = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % img.name.split('.')[0],
                                   'image/jpeg', sys.getsizeof(output_io_stream), None)
        return img


