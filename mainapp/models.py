# mainapp/models.py （既存に追記／上書き）
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    name = models.CharField(max_length=100, default='泉岡')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.name

class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='diary_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mainapp:diary_list')

class Stamp(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='stamps/')
    external_url = models.URLField(blank=True, help_text='LINEスタンプ販売ページ等のURL')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
