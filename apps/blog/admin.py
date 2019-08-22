from django.contrib import admin

from .models import BlogDir, BlogPost, BlogComment, BlogImage, Subscriber


@admin.register(BlogDir)
class BlogDirAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass

