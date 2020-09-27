from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import emp_infoSerializers
from .models import emp_info


# Create your views here.

@api_view(['GET'])
def api(request):
    api_urls = {
        'List': '/employeelist/',
        'Detail View': '/employee/<str:pk>/',
        'Create': '/create-employee/',
        'Update': '/update-employee/<str:pk>/',
        'Delete': '/S/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def employeelist(request):
    list = emp_info.objects.all()
    serializer = emp_infoSerializers(list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def employee(request, pk):
    print(request)
    view = emp_info.objects.get(id=pk)
    serializer = emp_infoSerializers(view, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_employee(request):
    serializer = emp_infoSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_employee(request, pk):
    delete = emp_info.objects.get(id=pk)
    serializer = emp_infoSerializers(instance=delete, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_employee(request, pk):
    task = emp_info.objects.get(id=pk)
    task.delete()
    return Response("Task Deleted Successfully")
