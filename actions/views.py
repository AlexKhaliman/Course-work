from django.views.decorators.http import require_GET
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from actions.add_category_form import AddingForm
from actions.register_form import RegistrationForm
from actions.models import User
from categories.models import Tasks, Categories, Offers


def create_task(request):

    if request.method == 'GET':
        return render(request, 'actions/add_task.html', context={
            'form': AddingForm(initial={'created_by': request.user.id})
        })

    elif request.method == 'POST':
        form = AddingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


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


def account(request, user_id):
    amount_of_offers = []
    tasks = Tasks.objects.filter(created_by=user_id)
    for task in tasks:
        amount_of_offers.append((Offers.objects.filter(task=task)).count())
    return render(request, "actions/account.html", context={
        'tasks': zip(tasks, amount_of_offers)
    })


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


def accept(request, user_id, task_id, offer_id):
    user = User.objects.get(id=user_id)
    offer = Offers.objects.get(id=offer_id)
    if request.method == 'GET':
        return render(request, 'actions/accept.html', context={
            'user': user,
            'offer': offer
        })
    elif request.method == 'POST':
        obj = Tasks.objects.get(id=task_id)
        obj.status = 'in process'
        obj.save()

        url = f"/account/{user.id}/"
        return redirect(url)


def get_offers(request, user_id, task_id):
    offers = Offers.objects.filter(task=task_id)
    return render(request, 'actions/get_offers.html', context={
        'offers': offers
    })
