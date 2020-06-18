from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:ph>/',
        'Delete':'/task-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    lista = Task.objects.all()
    serialize = TaskSerializer(lista, many = True)

    return Response(serialize.data)


@api_view(['GET'])
def task_list(request):
    lista = Task.objects.all()
    lista = lista[::-1]
    serialize = TaskSerializer(lista, many = True)

    return Response(serialize.data)


@api_view(['GET'])
def task_detail(request, pk):
    obj = Task.objects.get(id = pk)
    serialize = TaskSerializer(obj)

    return Response(serialize.data)


@api_view(['POST'])
def task_create(request):
    serialize = TaskSerializer(data = request.data)
    if serialize.is_valid():
        serialize.save()

    return Response(serialize.data)

@api_view(['POST'])
def task_update(request, pk):
    obj = Task.objects.get(id = pk)
    serialize = TaskSerializer(instance = obj,data = request.data)
    if serialize.is_valid():
        serialize.save()

    return Response(serialize.data)

@api_view(['DELETE'])
def task_delete(request, pk):
    obj = Task.objects.get(id = pk)
    obj.delete()

    return Response('deleted')