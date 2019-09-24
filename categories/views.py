from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Categories


def get_categories(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/categories.html', context)


def get_tasks(request, category_id):
    task = Categories.objects.get(pk=category_id)
    context = {
        'task': task
    }
    return render(request, 'categories/tasks.html', context)