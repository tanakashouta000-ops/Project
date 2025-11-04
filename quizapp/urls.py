# quizapp/urls.py
from django.urls import path
from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),        # /quiz/
    path('create/', views.quiz_create, name='quiz_create'),
    path('<int:pk>/', views.quiz_detail, name='quiz_detail'),
]
