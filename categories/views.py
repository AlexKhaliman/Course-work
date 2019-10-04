from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Categories, Tasks

from datetime import datetime


def get_categories(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/categories.html', context)


def get_tasks(request, category_id):
    cat = Categories.objects.get(id=category_id)
    tasks = Tasks.objects.filter(category=cat)
    return render(request, 'categories/tasks.html', context={
        'tasks': tasks,
        'category_id': category_id,
    })


def get_details(request, category_id, task_id):
    task = Tasks.objects.get(id=task_id)
    return render(request, 'categories/details.html', context={"task": task})


def to_respond(request, category_id, task_id):
    task = Tasks.objects.get(id=task_id)
    return render(request, 'categories/to_respond.html', context={'task': task})
