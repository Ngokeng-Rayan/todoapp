from django.test import TestCase, Client
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        """Test que la création d'une tâche fonctionne et que completed est False par défaut."""
        task = Task.objects.create(title="Tâche de test")
        self.assertEqual(task.title, "Tâche de test")
        self.assertFalse(task.completed)
        self.assertEqual(str(task), "Tâche de test")

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title="Tâche existante")
        self.index_url = reverse('index')
        self.add_url = reverse('add_task')
        self.toggle_url = reverse('toggle_task', args=[self.task.id])
        self.delete_url = reverse('delete_task', args=[self.task.id])

    def test_index_view(self):
        """Test que l'index s'affiche avec le statut 200 et contient la tâche existante."""
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tâche existante")
        self.assertTemplateUsed(response, 'todo/index.html')

    def test_add_task_view(self):
        """Test l'ajout d'une nouvelle tâche via POST."""
        response = self.client.post(self.add_url, {'title': 'Nouvelle tâche ajoutée'})
        self.assertRedirects(response, self.index_url)
        self.assertEqual(Task.objects.count(), 2)
        self.assertTrue(Task.objects.filter(title='Nouvelle tâche ajoutée').exists())

    def test_add_task_empty_title(self):
        """Test qu'une tâche avec un titre vide n'est pas créée."""
        response = self.client.post(self.add_url, {'title': '   '})
        self.assertRedirects(response, self.index_url)
        self.assertEqual(Task.objects.count(), 1) # Seulement celle du setUp()

    def test_toggle_task_view(self):
        """Test la bascule de l'état completed d'une tâche."""
        self.assertFalse(self.task.completed)
        response = self.client.get(self.toggle_url)
        self.assertRedirects(response, self.index_url)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

        # Re-toggle
        self.client.get(self.toggle_url)
        self.task.refresh_from_db()
        self.assertFalse(self.task.completed)

    def test_delete_task_view(self):
        """Test la suppression d'une tâche."""
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.index_url)
        self.assertEqual(Task.objects.count(), 0)
