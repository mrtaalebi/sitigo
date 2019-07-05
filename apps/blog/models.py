from django.db import models
from ckeditor.fields import RichTextField


class BlogDir(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)


class BlogPost(models.Model):
    dir = models.ForeignKey('BlogDir', on_delete=models.CASCADE, related_name='posts', null=False, blank=False)

    title = models.CharField(max_length=50, unique=True, null=False, blank=False)
    headline = models.TextField(max_length=200, null=False, blank=False)
    text = RichTextField()
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)


class BlogComment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments', null=False, blank=False)

    author = models.CharField(max_length=20, null=False, blank=True, default="Unknown")
    text = models.TextField(max_length=200, null=False, blank=False)

