from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Text
from .forms import new_task_form

def index(request):

    task_form = new_task_form()

    tasks = Text.objects.all()

    context = {
        'tasks' : tasks,
        'task_form' : task_form
    }

    return render(request, 'todo/index.html', context)

@require_POST
def AddTask(request):
    task_form = new_task_form(request.POST)

    if task_form.is_valid():
        new_task = Text(text=request.POST['text'], description=request.POST['description'])
        new_task.save()

    return redirect('todo:index')

def task_done(request, text_id):
    task = Text.objects.get(pk=text_id)
    task.done = True
    task.save()

    return redirect('todo:index')

def delete_done(request):
    Text.objects.filter(done__exact=True).delete()

    return redirect('todo:index')

def delete_all(request):
    Text.objects.all().delete()

    return redirect('todo:index')