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
    category = Categories.objects.get(id=category_id)
    tasks = Tasks.objects.filter(category=category)
    return render(request, 'categories/tasks.html', context={
        'tasks': tasks,
        'category': category,
    })


def get_details(request, category_id, task_id):
    task = Tasks.objects.get(id=task_id)
    return render(request, 'categories/details.html', context={"task": task})


def to_respond(request, category_id, task_id):
    task = Tasks.objects.get(id=task_id)
    if request.method == 'GET':
        return render(request, 'categories/to_respond.html')
    elif request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['suggested_by'] = request.user.id
        request.POST['task'] = task.id
        form = RespondForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')



