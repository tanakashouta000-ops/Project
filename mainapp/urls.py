# mainapp/urls.py
from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('diary/', views.diary_list, name='diary_list'),
    path('diary/create/', views.diary_create, name='diary_create'),
    path('stamps/', views.stamp_list, name='stamp_list'),
    path('stamps/create/', views.stamp_create, name='stamp_create'),
    path('stamp-ads/', views.stamp_list, name='stamp_ads'),
]
