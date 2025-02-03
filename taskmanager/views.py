from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from taskmanager.forms import UserCreateForm
from taskmanager.models import Task


def start_page(request: HttpRequest) -> HttpResponse:
    return render(request, "taskmanager/index.html")


class CustomLoginView(LoginView):
    def get_success_url(self):
        username = self.request.user.username
        return reverse("taskmanager:task_list",
                       kwargs={"username": username})


class CreateUserView(generic.CreateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = "taskmanager/create_user.html"

    def get_success_url(self):
        username = self.object.username
        return reverse_lazy("taskmanager:task_list",
                            kwargs={"username": username})


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "taskmanager/task_list.html"
