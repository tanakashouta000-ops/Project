# quizapp/admin.py
from django.contrib import admin
from .models import Quiz, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuizAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Quiz, QuizAdmin)
