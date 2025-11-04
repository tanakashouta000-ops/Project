# mainapp/views.py （既存に追記／上書き）
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Diary, Stamp
from django.views.decorators.http import require_http_methods

def home(request):
    profile = Profile.objects.first()
    return render(request, 'mainapp/home.html', {'profile': profile})

def diary_list(request):
    diaries = Diary.objects.order_by('-created_at')
    return render(request, 'mainapp/diary_list.html', {'diaries': diaries})

@require_http_methods(["GET", "POST"])
def diary_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image = request.FILES.get('image')
        if title and content:
            Diary.objects.create(title=title, content=content, image=image)
            return redirect('mainapp:diary_list')
    return render(request, 'mainapp/diary_create.html')

@require_http_methods(["GET", "POST"])
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(pk=1)
    if request.method == 'POST':
        profile.name = request.POST.get('name', profile.name)
        profile.bio = request.POST.get('bio', profile.bio)
        avatar = request.FILES.get('avatar')
        if avatar:
            profile.avatar = avatar
        profile.save()
        return redirect('mainapp:home')
    return render(request, 'mainapp/profile_edit.html', {'profile': profile})

# スタンプ一覧
def stamp_list(request):
    stamps = Stamp.objects.order_by('-created_at')
    return render(request, 'mainapp/stamp_list.html', {'stamps': stamps})

@require_http_methods(["GET", "POST"])
def stamp_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        image = request.FILES.get('image')
        external_url = request.POST.get('external_url', '').strip()
        if title and image:
            Stamp.objects.create(title=title, description=description, image=image, external_url=external_url)
            return redirect('mainapp:stamp_list')
    return render(request, 'mainapp/stamp_create.html')
