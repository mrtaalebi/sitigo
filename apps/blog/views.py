from django.shortcuts import render, redirect
from django.utils import translation

from .models import *
from .forms import BlogCommentForm


def blog_dir(request, dir_id=None):
    post_dirs = BlogDir.objects.filter(lang=translation.get_language())
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
                'id': adir.pk,
                'name': adir.name,
                'posts': [
                    {
                        'pk': post.pk,
                        'title': post.title,
                        'text': post.text,
                        'image': post.image,
                        'date_created': post.date_created,
                        'short_text': post.headline
                    }
                    for post in BlogPost.objects.filter(dir=adir).order_by('-date_created')],
            }
            for adir in post_dirs]
        context['current_dir_name'] = current_dir.name
        return render(request, 'blog/dir.html', context=context)


def blog_post(request, dir_id, post_id):
    if BlogPost.objects.filter(id=post_id, dir__id=dir_id).count() == 1:
        post = BlogPost.objects.get(id=post_id, dir__id=dir_id)
    else:
        return redirect('/')
    if post.dir.lang != translation.get_language():
        return redirect('/')

    context = {
        'post': post,
        'post_id': post_id,
        'dir_id': dir_id,
        'comments': BlogComment.objects.filter(post=post),
        'form': BlogCommentForm()
    }

    return render(request, 'blog/post.html', context)


def subscribe(request):
    if request.method == 'POST':
        if 'email' not in request.POST:
            return redirect(request, 'homepage')
        Subscriber.objects.create(email=request.POST['email'])
    return render(request, 'blog/subscripted.html')


def leave_comment(request, dir_id, post_id):

    if request.POST:
        form = BlogCommentForm(reqeust.POST)
        if form.is_valid():
            form.save()
    return blog_post(request, dir_id, post_id)
