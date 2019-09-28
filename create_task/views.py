from django.shortcuts import render
from django.http import HttpResponse


def create_task(request):
    return HttpResponse('Здесь должна быть форма заполнения')
