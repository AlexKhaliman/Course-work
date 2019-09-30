from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse


def create_task(request):
    return HttpResponse('Здесь должна быть форма заполнения')


def welcome(request):
    return render(request, 'actions/welcome.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, "actions/login.html", context={
            "error": False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            print(request.GET.get('next'))
            return redirect('/')
        else:
            return render(request, "actions/login.html", context={
                "error": True
            })


def logout_view(request):
    logout(request)
    return redirect("/")


def register(request):
    return HttpResponse('Здесь должная быть форма регистрации')


def account(request):
    return HttpResponse('личный кабинет')
