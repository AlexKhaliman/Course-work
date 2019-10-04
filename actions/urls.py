from django.urls import path

from . import views

urlpatterns = [
    path('creating/', views.create_task, name='create_task'),
    path('login/', views.login_view, name='login'),
    path('', views.welcome, name="welcome"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('account/<int:user_id>/', views.account, name="account"),
]

