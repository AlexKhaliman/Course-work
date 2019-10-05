from django.shortcuts import render, redirect

from .models import User
from .models import Categories, Tasks
from categories.respond_form import RespondForm


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
    if request.method == 'GET':
        task = Tasks.objects.get(id=task_id)
        print(request.user.id)
        return render(request, 'categories/to_respond.html', context={
            'form': RespondForm(initial={
                'suggested_by': request.user.id,
                'task': task.id
            })
        })
    elif request.method == 'POST':
        form = RespondForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')



