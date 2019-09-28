from django.urls import path

from . import views

urlpatterns = [
    path('creating/', views.create_task, name='create_task'),
    path('login/', views.login_view, name='login'),
]

