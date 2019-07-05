from django.contrib import admin

from .models import BlogDir, BlogPost, BlogComment


@admin.register(BlogDir)
class BlogDirAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass

