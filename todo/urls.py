from django.urls import path
from .views import *

# urlpatterns = [
#     path('tasks/', TodoListView.as_view(), name='list-create-tasks'),
#     path('tasks/<int:pk>/', CustomizeTodoView.as_view(), name='retrieve-update-delete-task'),
#     path('tasks/bulk_add/', BulkAddTodoView.as_view(), name='bulk-add-tasks'),
#     path('tasks/bulk_delete/', BulkDeleteTodoView.as_view(), name='bulk-delete-tasks'),
# ]

urlpatterns = [
    path('tasks', TodoView.as_view(), name='tasks'),
    path('tasks/<int:pk>', RetrieveUpdateDeleteTodoView.as_view(), name='retrieve-update-delete-task'),
    path('tasks/bulk_add/', BulkAddTodoView.as_view(), name='bulk-add-tasks'),
    path('tasks/bulk_delete/', BulkDeleteTodoView.as_view(), name='bulk-delete-tasks'),
]