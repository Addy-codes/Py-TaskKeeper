from django.urls import path
from .views import TodoListView, CustomizeTodoView

urlpatterns = [
    path('tasks/', TodoListView.as_view()),
    path('tasks/<int:pk>/', CustomizeTodoView.as_view()),
]
