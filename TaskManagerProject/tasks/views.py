from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task

# Home page showing all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Task Detail Page
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Create Task Page
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        messages.success(request, 'Task created successfully!')
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

# Mark task as completed
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    messages.success(request, 'Task marked as completed!')
    return redirect('task_list')

# Delete task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('task_list')
