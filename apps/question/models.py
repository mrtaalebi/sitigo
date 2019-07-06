from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Question(models.Model):
    LANG_CHOICES = (
        ('fa', _('persian')),
        ('en', _('english'))
    )
    language = models.CharField(choices=LANG_CHOICES, max_length=128, default='fa')
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)

    def __str__(self):
        return self.question
