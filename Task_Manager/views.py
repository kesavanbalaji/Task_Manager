from django.shortcuts import render,redirect
from Task_Manager.models import Task

# Views
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']
        Task.objects.create(title=title, description=description, priority=priority, status=status)
        return redirect('index')
    return render(request, 'add_task.html')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.priority = request.POST['priority']
        task.status = request.POST['status']
        task.save()
        return redirect('index')
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def filter_tasks(request):
    priority = request.GET.get('priority')
    tasks = Task.objects.filter(priority=priority) if priority else Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})
