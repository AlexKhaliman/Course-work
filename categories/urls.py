from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_categories, name='categories'),
    path('<int:category_id>/', views.get_tasks, name='tasks'),
    path('<int:category_id>/<int:task_id>/', views.get_details, name='details'),
    path('<int:category_id>/<int:task_id>/to_respond/', views.to_respond, name='to_respond')
]