from django.shortcuts import render

from .models import *

def blog_dir(request, dir_id=None):
    post_dirs = BlogDir.objects.all()
    if dir_id is not None and post_dirs.filter(pk=dir_id).count() == 1:
        current_dir = post_dirs.get(pk=dir_id)
    else:
        if post_dirs.count() > 0:
            current_dir = list(post_dirs)[-1]
            dir_id = current_dir.id
    context = {}
    if dir_id is None:
        return render(request, 'blog/dir.html', context=context)
    else:
        context['dirs'] = [
            {
                'pk': adir.pk,
                'name': adir.name,
                'posts': [
                    {
                        'title': post.title,
                        'text': post.text,
                        'image': post.image,
                        'date_created': post.date_created,
                        'short_text': post.text[0: 300]
                    }
                    for post in BlogPost.objects.filter(dir=adir).order_by('-date_created')],
            }
            for adir in post_dirs]
        context['current_dir_name'] = current_dir.name
        return render(request, 'blog/dir.html', context=context)


def blog_post(request, dir_id, post_id):
    if BlogPost.objects.filter(pk=dir_id).count() == 1:
        post = BlogPost.objects.get(pk=dir_id)
    else:
        return redirect(request.path)
    
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


