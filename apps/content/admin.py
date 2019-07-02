from django.contrib import admin

from .models import Post, FileUpload


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    pass

