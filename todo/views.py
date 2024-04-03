from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-updated_at')
    data = {'tasks': tasks}
    return render(request, 'todo/home.html', data)

def add_task(request):
    if request.method == 'POST':
        task = request.POST['add_task']
        Task.objects.create(task=task)

    return redirect('todo:home')

