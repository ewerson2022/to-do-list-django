from django.test import TestCase
from django.urls import reverse
from .models import Task

class TasklistViewTests(TestCase):

    def setUp(self):
        self.task1 = Task.objects.create(title="Tarefa 1", description="Description 1", completed=False)
        self.task2 = Task.objects.create(title="Tarefa 2", description="Description 2", completed=True)

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarefa 1")
        self.assertContains(response, "Tarefa 2")
        self.assertTemplateUsed(response, 'tasks/task_list.html')
