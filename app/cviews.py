from app.models import Todos
from .serializer import TodosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TodoList(APIView):
    def get(self,request):
        todos = Todos.objects.all()
        serializer = TodosSerializer(todos,many=True)
        return Response(serializer.data) 
    def post(self,request):
        serializer = TodosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
 
class TodoDetails(APIView):
    def get(self,request,pk):
        todos = Todos.objects.get(id = pk)
        serializer = TodosSerializer(todos,many=False )
        return Response(serializer.data)
    def put(self,request,pk):
        todo = Todos.objects.get(id = pk)
        serializer = TodosSerializer(instance=todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def patch(self,request,pk):
        todo = Todos.objects.get(id = pk)
        serializer = TodosSerializer(instance=todo,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self,request,pk):
        todo = Todos.objects.get(id = pk)
        todo.delete()
        return Response('Delete succesfull')

# @api_view(['DELETE'])
# def tododelete(request,pk): 
#     todo = Todos.objects.get(id = pk)
#     todo.delete()
#     return Response('Delete succesfull')