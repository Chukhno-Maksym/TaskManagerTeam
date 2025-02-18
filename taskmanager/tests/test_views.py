import json
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from taskmanager.models import Task, TaskType


class TaskManagerTestViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.task_type = TaskType.objects.create(name="Task Type")

        self.task = Task.objects.create(
            name="Task Name",
            description="Task Description",
            task_type=self.task_type,
            deadline=datetime.now(),
        )

        self.client = Client()
        self.client.login(username="testuser", password="testpassword123")

    def test_task_list_view(self):
        url = reverse("taskmanager:tasks")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_task_view(self):
        url = reverse("taskmanager:create_task")
        data = {
            "name": "testtask",
            "description": "testtask",
            "assignee": [self.user.id],
        }
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

    def test_update_task_view(self):
        url = reverse("taskmanager:task_update", kwargs={"pk": self.task.pk})
        data = {
            "name": "testtask1",
            "description": "testtask1",
            "deadline": (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
            "task_type": "testtype1",
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

    def test_detail_task_view(self):
        url = reverse("taskmanager:task_detail", kwargs={"pk": self.task.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_delete_task_view(self):
        url = reverse("taskmanager:task_delete", kwargs={"pk": self.task.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse("taskmanager:tasks"))

    def test_create_user(self):
        url = reverse("taskmanager:create_user")
        data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "email": "test@example.com",
        }
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

    def test_user_detail_view(self):
        url = reverse("taskmanager:user_info")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        url = reverse("taskmanager:user_update")
        data = {
            "username": "testuser1",
            "password1": "testpassword1231",
            "password2": "testpassword1231",
            "email": "test1@example.com",
        }
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        url = reverse("taskmanager:user_delete")
        response = self.client.post(url)
        self.assertRedirects(response, reverse("login"))
