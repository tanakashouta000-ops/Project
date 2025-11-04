# mainapp/admin.py
from django.contrib import admin
from .models import Profile, Diary, Stamp

admin.site.register(Profile)
admin.site.register(Diary)
admin.site.register(Stamp)
