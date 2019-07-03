import mimetypes
import os
import urllib
from urllib.parse import unquote

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import translate_url
from django.utils.http import is_safe_url
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, )

from apps.content.models import Age

LANGUAGE_QUERY_PARAMETER = 'language'


def age(request):
    prev_ages = list(Age.objects.all().order_by('year'))
    x = []
    for p_age in prev_ages:
        x.append({
            'id': p_age.id,
            'year': p_age.year,
            'name': p_age.name,
            # 'files': list(p_age.files.all()),
            # 'poster': p_age.poster
        })
    context = {'prev_ages': x}
    if request.method == 'POST':
        active = Age.objects.get(id=request.POST.get('id', False))
    else:
        if len(prev_ages) > 0:
            active = prev_ages[len(prev_ages)-1]
        else:
            active = None
    if active is not None:
        ctx = {
            'id': active.id,
            'name': active.name,
            'year': active.year,
            'persian_content': active.persian_content,
            'english_content': active.english_content,
            'files': list(active.files.all()),
            'poster': active.poster
        }
        context.update({'active': ctx})
    return render(request, 'content/age.html', context)


def doc_dwnldr(request):
    print(request)
    file_path = request.POST['file_path']
    original_filename = request.POST['original_file_name']
    fp = open(file_path, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type, encoding = mimetypes.guess_type(original_filename)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(file_path).st_size)
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
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(original_filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response
