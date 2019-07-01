from django.shortcuts import render


def homepage(request):
    print(request.LANGUAGE_CODE)
    return render(request, 'intro/homepage.html')

