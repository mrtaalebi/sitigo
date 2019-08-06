from django.db import models
import sys
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

from apps.content.models import Event


class Team(models.Model):
    persian_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    position_from_top = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.english_name + " " + str(self.position_from_top) + " - " + str(self.event)


class Role(models.Model):
    persian_name = models.CharField(max_length=300)
    english_name = models.CharField(max_length=300)
    
    is_head = models.BooleanField(default=False)

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.english_name


class Staff(models.Model):
    persian_firstname = models.CharField(max_length=300)
    persian_lastname = models.CharField(max_length=300)
    english_firstname = models.CharField(max_length=300)
    english_lastname = models.CharField(max_length=300)

    image = models.ImageField(upload_to='staff_photos', default='staff-default.png')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


    def __str__(self):
        return self.english_firstname + " " + self.english_lastname

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


class AddEmAll(models.Model):
    team_csv = models.FileField(upload_to='addemall')
    role_csv = models.FileField(upload_to='addemall')
    data_csv = models.FileField(upload_to='addemall')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(AddEmAll, self).save(*args, **kwargs)

        from apps.staff.management.commands.addemall import Command
        if Command().addemall(
                str(self.team_csv.file),
                str(self.role_csv.file),
                str(self.data_csv.file),
                self.event.id
            ) != 0:
            return


