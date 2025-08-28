from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404
from django.utils import timezone

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa criada com sucesso!")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def task_list(request):
        tasks = Task.objects.all()
        return render(request, 'tasks/task_list.html', {'tasks': tasks, 'today': timezone.now().date()})


def task_update(request, id):
     task = get_object_or_404(Task, id=id)
     if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa atualizada com sucesso!")
            return redirect('task_list')
     else:
        form = TaskForm(instance=task)

     return render(request, 'tasks/update_task.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, "Tarefa excluída com sucesso!")
    return redirect('task_list')

def toggle_complete(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    messages.success(request, "tarefa atualizada")
    return redirect('task_list')

        

