from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from taskmanager.forms import UserCreateForm, UserUpdateForm, TaskSearchForm, TaskCreateForm
from taskmanager.models import Worker, TaskType


class TestForms(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.worker = Worker.objects.create_user(username="worker", password="testpassword123")
        self.task_type = TaskType.objects.create(name="Type")

    def test_user_create_form(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "testpassword123",
        }

        form = UserCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_didnt_match(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "testpassword122",
        }

        form = UserCreateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_user_update_form(self):
        form_data = {
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "test@example.com",
        }

        form = UserUpdateForm(instance=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_valid_search(self):
        form_data = {
            "team": "Development Team",
            "status": "True",
            "priority": "high",
        }

        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_search(self):
        form_data = {
            "team": "Invalid Team",
            "status": "True",
            "priority": "high",
        }

        form = TaskSearchForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_task_create_form(self):
        form_data = {
            "name": "Task Name",
            "description": "Task Description",
            "task_type": self.task_type,
            "is_completed": True,
            "priority": "high",
            "deadline": datetime.now().strftime("%Y-%m-%dT%H:%M"),
            "assignees": [self.worker.id],
        }
        form = TaskCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
