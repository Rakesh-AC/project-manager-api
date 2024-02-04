from django.urls import path
from . import views


urlpatterns = [
    path("", views.url_list, name="home" ),

    # Project urls
    path('project-list/', views.project_list, name='project-list'),
    path('project-details/<int:pk>/', views.projectDetails, name='project-detail'),
    path('project-create/', views.projectCreate, name='project-detail'),
    path('project-update/<int:pk>/', views.projectUpdate, name='project-detail'),
    path('project-delete/<int:pk>/', views.projectDelete, name='project-detail'),

    # Task urls
    path('task-list/', views.taskList, name='task-list'),
    path('task-details/<int:pk>/', views.taskDetails, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-detail'),
    path('task-update/<int:pk>/', views.taskUpdate, name='task-detail'),
    path('task-delete/<int:pk>/', views.taskDelete, name='task-detail'),

]


