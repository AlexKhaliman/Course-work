from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_categories, name='categories'),
    path('<int:category_id>/', views.get_tasks, name='tasks')
]