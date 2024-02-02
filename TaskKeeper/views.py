from django.shortcuts import render
from django.db import transaction
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CustomizeTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class BulkAddTodoView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data, many=True)  # Note the `many=True` for bulk operations
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
