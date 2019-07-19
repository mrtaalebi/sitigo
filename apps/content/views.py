import mimetypes
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import translation


from apps.content.models import Event, Article, Category, SubCategory

LANGUAGE_QUERY_PARAMETER = 'language'


def event(request, event_id = None):
    prev_ages = list(Event.objects.all().order_by('year'))
    x = []
    for p_age in prev_ages:
        x.append({
            'id': p_age.id,
            'year': p_age.year,
            'persian_name': p_age.persian_name,
            'english_name': p_age.english_name,
            # 'files': list(p_age.files.all()),
            # 'poster': p_age.poster
        })
    context = {'prev_ages': x}
    if event_id is not None:
        active = Event.objects.get(id=event_id)
    else:
        if len(prev_ages) > 0:
            active = prev_ages[len(prev_ages)-1]
        else:
            active = None
    if active is not None:
        ctx = {
            'id': active.id,
            'persian_name': active.persian_name,
            'english_name': active.english_name,
            'year': active.year,
            'persian_content': active.persian_content,
            'english_content': active.english_content,
            'files': list(active.files.all()),
            'poster': active.poster,
            'images': list(active.images.all())
        }
        context.update({'active': ctx})
    return render(request, 'content/event.html', context)


def articles(request, category_id=None):
    categories = Category.objects.all()
    context = {'categories': list(categories)}
    if category_id is None:
        if len(categories) > 0:
            active = categories.filter(language=translation.get_language())
            if len(active) > 0:
                active = active[0]
                articles = Article.objects.filter(category=active)
            else:
                articles = []
                active = None

                context.update({
                'articles': articles,
                'sub_cats': [
                    {
                        'name': cat.name,
                        'articles': list(articles.objects.filter(sub_cat=cat))
                    }
                    for cat in SubCategory.objects.filter(cat=active)],
                'has_subs': SubCategory.objects.filter(cat=active).count() != 0,
                'active': active
                 })
        else:
            active = ''
            context.update({
                'articles': articles,
                'sub_cats': [
                    {
                        'name': cat.name,
                        'articles': list(articles.objects.filter(sub_cat=cat))
                    }
                    for cat in SubCategory.objects.filter(cat=active)],
                'has_subs': SubCategory.objects.filter(cat=active).count() != 0,
                'active': active
            })
    else:
        active = Category.objects.get(id=category_id)
        articles = Article.objects.filter(category=active)
        if Category.objects.get(id=category_id).language != translation.get_language():
            return redirect('/articles/')
        context.update({
                'articles': articles,
                'sub_cats': [
                    {
                        'name': cat.name,
                        'articles': list(articles.filter(sub_cat=cat))
                    }
                    for cat in SubCategory.objects.filter(cat=active)],
                'has_subs': SubCategory.objects.filter(cat=active).count() != 0,
                'active': active
        })

        if context['has_subs']:
            non_sub = list(articles)
            for cat in context['sub_cats']:
                for art in cat['articles']:
                    non_sub.remove(art)
            if len(non_sub) > 0:
                context['sub_cats'] += [{
                        'name': 'other',
                        'articles': non_sub
                    }]
 
    return render(request, 'content/articles.html', context)


def doc_dwnldr(request):
    file_path = request.POST['file_path']
    original_filename = request.POST['original_file_name']
    x = os.path.abspath(os.path.join(settings.MEDIA_ROOT, original_filename))
    print(x)
    fp = open(x, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type, encoding = mimetypes.guess_type(x)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(x).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding

    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % original_filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % original_filename
    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response
