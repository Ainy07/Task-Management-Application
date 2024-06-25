from django.shortcuts import render
from .models import Tasks

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = Tasks.objects.get(pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task, 'tasks': Tasks.objects.all()})