import mimetypes
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import translation

from apps.content.models import Age, Article, Category

LANGUAGE_QUERY_PARAMETER = 'language'

def faq(request):
    return render(request, 'content/faq.html')

def age(request):
    prev_ages = list(Age.objects.all().order_by('year'))
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
    if request.method == 'POST':
        print(request.POST)
        active = Age.objects.get(id=request.POST.get('id', 1))
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
            'poster': active.poster
        }
        context.update({'active': ctx})
    return render(request, 'content/age.html', context)


def articles(request):
    print(translation.get_language())
    categories = Category.objects.all()
    context = {'categories': list(categories)}
    if request.method == 'GET':
        if len(categories) > 0:
            active = categories.filter(language=translation.get_language())[0]
            print(active)
            articles = Article.objects.filter(category=active)
            context.update({
                'articles': articles
            })
        else:
            active = ''
        context.update({
                    'active': active
        })
    if request.method == 'POST':
        active_category_id = request.POST.get('id', 1)
        articles = Article.objects.get(category_id=active_category_id)
        context.update({
            'active': Article.objects.get(id= active_category_id),
            'articles': articles
        })
    print(context)
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
