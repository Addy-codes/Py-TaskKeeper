from django.shortcuts import render, get_object_or_404
from django.db import transaction
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer
from django.http import HttpResponse

class Home(APIView):
    def get(self, request,):
        return HttpResponse("Welcome to the Py-Task Keeper API")
    
class TodoView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()  # Save the instance and get the saved object
            # Return a response with only the id of the created task
            print("Saved Instance")
            print(saved_instance.id)
            return Response({'id': saved_instance.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response({'tasks': serializer.data})  # Wrap in "tasks" key


class RetrieveUpdateDeleteTodoView(APIView):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(task)
        return Response(serializer.data)
    def delete(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Todo, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view for bulk adding tasks
class BulkAddTodoView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data, many=True)  # Note the `many=True` for bulk operations
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# New view for bulk deleting tasks
class BulkDeleteTodoView(APIView):
    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])  # Expect a list of IDs to delete
        if not ids:
            return Response({"error": "No IDs provided for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            # Use `id__in` to filter tasks that match the list of provided IDs and delete them
            delete_count, _ = Todo.objects.filter(id__in=ids).delete()
        
        if delete_count:
            return Response({"message": f"Successfully deleted {delete_count} tasks."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "No tasks found matching the provided IDs."}, status=status.HTTP_404_NOT_FOUND)
