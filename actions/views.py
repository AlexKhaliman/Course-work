from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from actions.register_form import RegistrationForm
from actions.models import User
from django.views.decorators.http import require_GET


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


def account(request):
    return HttpResponse('личный кабинет')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.verify_email()
            return render(request, "actions/check_email.html")
    else:
        form = RegistrationForm()
    return render(request, "actions/register.html", context={
        "form": form
    })


@require_GET
def verify_email(request):
    key = request.GET.get("key")
    if request.user.check_key(key):
        request.user.is_email_verified = True
        request.user.save()
        return render(request, "actions/account_activated.html")
    return redirect("/")


