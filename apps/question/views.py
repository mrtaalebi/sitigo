from django.shortcuts import render
# Create your views here.
from django.utils import translation

from apps.question.models import FAQ


def question_answer(request):
    questions = list(FAQ.objects.filter(language=translation.get_language()))
    context = {'questions': questions}
    return render(request, 'question/question_answer.html', context)

