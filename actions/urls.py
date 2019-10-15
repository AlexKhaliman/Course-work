from django.urls import path

from . import views

urlpatterns = [
    path('creating/', views.create_task, name='create_task'),
    path('login/', views.login_view, name='login'),
    path('', views.welcome, name="welcome"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('account/<int:user_id>/', views.account, name="account"),
    path('account/<int:user_id>/comments/', views.comments, name="comments"),
    path('account/<int:user_id>/<int:task_id>/offers/', views.get_offers, name='offers'),
    path('account/<int:user_id>/<int:task_id>/offers/<int:offer_id>', views.accept, name='accept'),
    path('account/<int:user_id>/<int:task_id>/complete/', views.complete, name='complete'),
    path('account/<int:user_id>/<int:task_id>/complete/feedback', views.feedback, name='feedback')

]

