from django import forms
from captcha.fields import ReCaptchaField

from .models import BlogComment

class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = '__all__'

    captcha = ReCaptchaField

