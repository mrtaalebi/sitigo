from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)
