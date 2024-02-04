from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Task
from .serializers import ProjectSerializer,TaskSerializer
from django.shortcuts import render

@api_view(["GET"])
def url_list(request):
    project_url_list = {
        "List": '/project-list/',
        'Detail view': '/project-details/<int:pk>/',
        'Create': '/project-create/',
        'Update' : '/project-update/<int:pk>/',
        'Delete' : '/project-delete/<int:pk>/'
    }
    task_url_list = {
          "List": '/task-list/',
        'Detail view': '/task-details/<str:pk>/',
        'Create': '/task-create/',
        'Update' : '/task-delete/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/'
    }
    api_urls = {
       "Project": project_url_list, "Task":task_url_list
    }
    return Response(api_urls)


@api_view(['GET'])
def project_list(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projectDetails(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=404)

    project_serializer = ProjectSerializer(project, many=False)
    tasks = Task.objects.filter(project=project)
    task_serializer = TaskSerializer(tasks, many=True)

    return Response({
        "project_details": project_serializer.data,
        "tasks": task_serializer.data
    })


@api_view(["POST"])
def projectCreate(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def projectUpdate(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def projectDelete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return Response("Project is successfully deleted")




# Task urls ---------------------------------
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    


@api_view(["DELETE"])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item Successfully deleted")