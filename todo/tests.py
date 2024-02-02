from django.test import TestCase
from .models import Todo

class TodoTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Create a tasks
        test_todo = Todo.objects.create(
            title='My First Task',
            is_completed=False)
        test_todo.save()

    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        title = f'{todo.title}'
        is_completed = f'{todo.is_completed}'
        self.assertEqual(title, 'My First Task')
        self.assertTrue(is_completed, False)
