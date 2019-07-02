from django import forms
from captcha.fields import ReCaptchaField

from .models import ContactInfo

class ContactInfoForm(forms.Form):

    class Meta:
        model = ContactInfo
        fields = '__all__'
        #captcha = ReCaptchaField()

