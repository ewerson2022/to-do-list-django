from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),    
    path('create/', views.create_task, name='create_task'),
    path('update/<int:id>/', views.task_update, name='task_update'), 
    path('delete/<int:id>/',views.task_delete, name='task_delete'),
    path('toggle/<int:id>/', views.toggle_complete, name='toggle_complete')

]