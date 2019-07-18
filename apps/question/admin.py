from django.contrib import admin

# Register your models here.
from apps.question.models import FAQ


@admin.register(FAQ)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['language', 'question', 'answer']
