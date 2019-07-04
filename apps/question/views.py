from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils import translation

from apps.question.models import Question


def question_answer(request):
    if translation.get_language() == 'en':
        return HttpResponseRedirect('/intro/')
    questions = list(Question.objects.all())
    context = {'questions': questions}
    return render(request, 'question/question_answer.html', context)

