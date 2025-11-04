# quizapp/models.py
from django.db import models
from django.urls import reverse

class Quiz(models.Model):
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]

class Choice(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'正解' if self.is_correct else '不正解'})"
