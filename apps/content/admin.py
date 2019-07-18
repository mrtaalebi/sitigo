from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.content.models import ImageUpload
from .models import FileUpload, Event, Category, SubCategory, Article


@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    fields = ['image', 'caption']


class FileUploadAdmin(forms.ModelForm):
    fields = ['file', 'name', 'thumbnail']

    class Meta:
        fields = ['file', 'name', 'thumbnail']
        model = FileUpload


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    form = FileUploadAdmin
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['persian_name', 'english_name', 'poster', 'persian_content', 'english_content', 'files', 'year', 'images']
    # inlines = [FileInLine,]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['language', 'name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fields = ['category', 'name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['category', 'sub_cat', 'file']

