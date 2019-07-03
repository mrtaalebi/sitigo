from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, FileUpload, Age


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


class FileUploadAdmin(forms.ModelForm):
    fields = ['file', 'name', 'image']

    class Meta:
        fields = ['file', 'name', 'image']
        model = FileUpload


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    form = FileUploadAdmin
    pass


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    fields = ['persian_name', 'english_name', 'poster', 'persian_content', 'english_content', 'files', 'year']
    # inlines = [FileInLine,]

