from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Hint, Task


class HintTests(APITestCase):
    def setUp(self):
        admin = User.objects.create_superuser(username="test")
        self.client.force_authenticate(user=admin)
        self.task = Task.objects.create(title="test")

    def test_create_hint(self):
        """
        Ensure we can create a hint.
        """
        url = f"/hints/"
        data = {"hint": "test", "task": self.task.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hint.objects.count(), 1)

    def test_edit_hint(self):
        """
        Ensure we can edit a hint.
        """
        url = f"/hints/"
        data = {"hint": "test", "task": self.task.id}
        response = self.client.post(url, data, format="json")
        url = f"/hints/{response.data['id']}/"
        data = {"id": response.data["id"], "hint": "changed"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hint.objects.get(id=response.data["id"]).hint, "changed")

    def test_perms(self):
        """
        Ensure perms work
        """
        self.client.logout()
        url = f"/hints/"
        data = {"hint": "test", "task": self.task.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
