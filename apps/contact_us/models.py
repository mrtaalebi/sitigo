from django.db import models
from ckeditor.fields import RichTextField

from django.core.validators import RegexValidator

from django.utils.translation import ugettext, ugettext_lazy as _

class ContactInfo(models.Model):

    study_grade_choices = (('middle school', _('middle school')),
            ('high school', _('high school')),
            ('university', _('university')),
            )

    name = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False, default='ran, Islamic Republic of')
    school_uni = models.CharField(max_length=50, null=False, blank=False)
    study_grade = models.CharField(max_length=50, choices=study_grade_choices, null=False, blank=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,19}$', message="Phone number must be entered in the format with region code: '+999999999'. Up to 18 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    email = models.EmailField(max_length=50, null=False, blank=False)

    subject = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(max_length=500, null=False, blank=False)
