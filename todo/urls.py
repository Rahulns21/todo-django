from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add-task'),
    path('task-complete/<str:slug>/', views.task_complete, name='task-complete'),
    path('task-undone/<str:slug>/', views.task_undone, name='task-undone'),
    path('edit-task/<str:slug>/', views.edit_task, name='edit-task'),
    path('delete-task/<str:slug>/', views.delete_task, name='delete-task'),
]
