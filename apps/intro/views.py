from django.shortcuts import render

# Create your views here.
def homepage(request):
    print(request.LANGUAGE_CODE)
    return render(request, 'intro/homepage.html')