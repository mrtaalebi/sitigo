from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    content = RichTextField()


class FileUpload(models.Model):
    name = models.CharField(max_length=50)
    file = RichTextUploadingField()


class Age(models.Model):
    poster = models.ImageField()
    files = models.ManyToManyField(FileUpload)





