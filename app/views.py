from django.shortcuts import render,get_object_or_404
from app.models import Todos
from .serializer import TodosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def todolist(request):
    todos = Todos.objects.all()
    serializer = TodosSerializer(todos,many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def tododetails(request,pk):
    todos = Todos.objects.get(id = pk)
    serializer = TodosSerializer(todos,many=False )
    return Response(serializer.data)

@api_view(['POST'])
def todoadd(request): 
    serializer = TodosSerializer(data=request.data)
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def todoupdate(request,pk): 
    todo = Todos.objects.get(id = pk)
    serializer = TodosSerializer(instance=todo,data=request.data)
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def tododelete(request,pk): 
    todo = Todos.objects.get(id = pk)
    todo.delete()
    return Response('Delete succesfull')