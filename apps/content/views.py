from urllib.parse import unquote

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import translate_url
from django.utils.http import is_safe_url
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, )

LANGUAGE_QUERY_PARAMETER = 'language'


def age (request):
    print(request.LANGUAGE_CODE)
    return render(request, 'content/age.html')