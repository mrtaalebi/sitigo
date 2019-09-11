# Create your views here.
from urllib.parse import unquote

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import translate_url
from django.utils.http import is_safe_url
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, )

from apps.intro.models import HomePage, HomePageImage

from apps.gallery.models import Image
import random

from apps.blog.models import BlogPost
from django.utils import translation

LANGUAGE_QUERY_PARAMETER = 'language'


def homepage(request):
    context = {}
    if len(HomePage.objects.all()) > 0:
        hp = HomePage.objects.all()[0]
        sponsor = {
            'persian_name': hp.sponsor_name_persian,
            'english_name': hp.sponsor_name_english,
            'image': hp.sponsor_image
        }
        organizer = {
            'persian_name': hp.organizer_name_persian,
            'english_name': hp.organizer_name_english,
            'image': hp.organizer_image
        }
        context.update({
            'sponsor': sponsor,
            'organizer': organizer
        })
    gallery_images = list(Image.objects.all())
    if len(gallery_images) > 0:
        images = random.sample(gallery_images, min(9, len(gallery_images)))
    else:
        images = []
    context.update({
        'slideshow': [{
            'image': img,
            'link': '/gallery/{}/{}#{}'.format(img.country_event.event.id,
                                            img.country_event.gallery.id if img.country_event.gallery is not None else '',
                                            img.country_event.country.english_name),
            } for img in images],
        'num_of_img': range(len(images)),
    })

    blog_posts = BlogPost.objects.filter(dir__lang=translation.get_language()).order_by('-date_created')
    blog_posts = blog_posts[0:min(4, len(blog_posts))]
    context['blog_posts'] = list(blog_posts)
    return render(request, 'intro/homepage.html', context)


def set_lang(request):
    """
    Redirect to a given URL while setting the chosen language in the session
    (if enabled) and in a cookie. The URL and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = request.POST.get('next', request.GET.get('next'))
    if ((next or not request.is_ajax()) and
            not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure())):
        next = request.META.get('HTTP_REFERER')
        next = next and unquote(next)  # HTTP_REFERER may be encoded.
        if not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
            next = '/'
    response = HttpResponseRedirect(next) if next else HttpResponse(status=204)
    if request.method == 'POST':
        lang_code = request.POST.get(LANGUAGE_QUERY_PARAMETER)
        if lang_code and check_for_language(lang_code):
            if next:
                next_trans = translate_url(next, lang_code)
                if next_trans != next:
                    response = HttpResponseRedirect(next_trans)
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = lang_code
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME, lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
            )
    return response
