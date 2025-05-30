from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('tasks/create/', views.create_task, name = 'create_task'),
    path('tasks/update/<int:task_id>', views.update_task, name = 'update_task'),
    path('tasks/delete/<int:task_id>', views.delete_task, name = 'delete_task'),
]

