from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, FileUpload, Age


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


class FileUploadAdmin(forms.ModelForm):
    fields = ['file', 'name', 'image']

    file = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        fields = ['file', 'name', 'image']
        model = FileUpload


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    form = FileUploadAdmin
    pass


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    fields = ['poster', 'content', 'files', 'year']
    # inlines = [FileInLine,]

