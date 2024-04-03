from django.shortcuts import render, redirect, get_object_or_404
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

def task_complete(request, slug):
    task = get_object_or_404(Task, slug=slug)
    task.is_completed = True
    task.save()
    return redirect('todo:home')

def task_undone(request, slug):
    task =get_object_or_404(Task, slug=slug)
    task.is_completed = False
    task.save()
    return redirect('todo:home')

def edit_task(request, slug):
    get_task = get_object_or_404(Task, slug=slug)
    if request.method == 'POST':
        updated_task = request.POST['edit_task']
        get_task.task = updated_task
        get_task.save()
        return redirect('todo:home')
    else:
        data = {'get_task': get_task}
    return render(request, 'todo/edit_task.html', data)

def delete_task(request, slug):
    delete_task = get_object_or_404(Task, slug=slug)
    delete_task.delete()
    return redirect('todo:home')