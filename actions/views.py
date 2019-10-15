from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from actions.add_category_form import AddingForm
from actions.register_form import RegistrationForm
from actions.models import User
from categories.models import Tasks, Categories, Offers, Comments


def create_task(request):
    categories = Categories.objects.all()
    if request.method == 'GET':
        return render(request, 'actions/add_task.html', context={
            'categories': categories
        })

    elif request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['created_by'] = request.user.id
        category_id = request.POST['category']
        request.POST['category'] = Categories.objects.get(id=category_id).id
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
    comments = Comments.objects.filter(for_whom=user_id)
    pos_comments = [i for i in comments if i.is_positive==True]

    for task in tasks:
        amount_of_offers.append((Offers.objects.filter(task=task)).count())
    return render(request, "actions/account.html", context={
        'tasks': zip(tasks, amount_of_offers),
        'comments': comments,
        'pos_comments': pos_comments,
        'neg_comments': len(comments) - len(pos_comments)
    })


def comments(request, user_id):
    comments = Comments.objects.filter(for_whom=user_id)
    return render(request, 'actions/comments.html', context={
        'comments': comments
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
        return render(request, "actions/register.html")


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

    if request.method == 'GET':
        offer = Offers.objects.get(id=offer_id)
        return render(request, 'actions/accept.html', context={
            'user': user,
            'offer': offer
        })
    elif request.method == 'POST':
        offers = Offers.objects.filter(task=task_id)
        for offer in offers:
            if offer.id != offer_id:
                offer.delete()
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


def complete(request, user_id, task_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        task = Tasks.objects.get(id=task_id)
        return render(request, 'actions/complete.html', context={
            'task': task,
            'user': user
        })
    elif request.method == 'POST':
        task = Tasks.objects.get(id=task_id)
        offer = Offers.objects.get(task=task_id)
        if '_complete' in request.POST:
            task.delete()

        elif '_cancel' in request.POST:

            task.status = 'looking for executor'
            task.save()

        offer.delete()
        return render(request, 'actions/feedback.html', context={
            'offer': offer,
            'task': task
        })


def feedback(request, user_id, task_id):
    url = f"/account/{user_id}/"
    text = request.POST.get('post_text')
    owner = request.POST.get('post_owner')
    form = Comments(text=text, from_whom=request.user.id, for_whom=owner)
    form.save()
    return redirect(url)
