# quizapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Choice
from django.views.decorators.http import require_http_methods

def quiz_list(request):
    quizzes = Quiz.objects.order_by('-created_at')
    return render(request, 'quizapp/quiz_list.html', {'quizzes': quizzes})

@require_http_methods(["GET", "POST"])
def quiz_create(request):
    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        choices = [request.POST.get(f'choice{i}', '').strip() for i in range(1,5)]
        correct = request.POST.get('correct')
        if question and all(choices):
            q = Quiz.objects.create(question=question)
            for i,text in enumerate(choices, start=1):
                Choice.objects.create(quiz=q, text=text, is_correct=(str(i)==correct))
            return redirect('quizapp:quiz_list')
    return render(request, 'quizapp/quiz_create.html')

@require_http_methods(["GET", "POST"])
def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        selected = request.POST.get('choice')
        if not selected:
            result = {'error': '選択肢が選ばれていません。'}
        else:
            choice = get_object_or_404(Choice, pk=int(selected))
            result = {'correct': choice.is_correct, 'selected': choice, 'quiz': quiz}
        return render(request, 'quizapp/quiz_result.html', result)
    return render(request, 'quizapp/quiz_detail.html', {'quiz': quiz})
