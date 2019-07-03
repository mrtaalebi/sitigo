from django import forms
from captcha.fields import ReCaptchaField

from .models import ContactInfo

class ContactInfoForm(forms.Form):

    class Meta:
        model = ContactInfo
        fields = '__all__'

    name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=50, required=True)

    country = forms.CharField(max_length=50, required=True)
    school_uni = forms.CharField(max_length=50, required=True)
    study_grade = forms.CharField(max_length=50, required=True)

    subject = forms.CharField(max_length=100, required=True)
    text = forms.CharField(max_length=500, widget=forms.Textarea, required=True)

#    captcha = ReCaptchaField()

