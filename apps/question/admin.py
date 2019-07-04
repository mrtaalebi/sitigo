from django.contrib import admin

# Register your models here.
from apps.question.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question', 'answer']
