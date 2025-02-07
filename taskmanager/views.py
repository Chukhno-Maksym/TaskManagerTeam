from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from taskmanager.forms import (
    UserCreateForm,
    TaskSearchForm,
    TaskCreateForm,
    UserUpdateForm,
)
from taskmanager.models import Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "taskmanager/index.html")


class CreateUserView(generic.CreateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = "taskmanager/create_user.html"
    success_url = reverse_lazy("taskmanager:tasks")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "taskmanager/user_info.html"

    def get_object(self):
        return self.request.user


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = "taskmanager/user_confirm_delete.html"
    success_url = reverse_lazy("login")

    def get_object(self):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "taskmanager/user_form.html"
    success_url = reverse_lazy("taskmanager:user_info")

    def get_object(self):
        return self.request.user


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "taskmanager/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = Task.objects.all()
        search_form = TaskSearchForm(self.request.GET)
        assigned_to = self.request.GET.get("assigned_to")

        if search_form.is_valid():
            team = search_form.cleaned_data.get("team")
            status = search_form.cleaned_data.get("status")
            priority = search_form.cleaned_data.get("priority")

            if assigned_to == "me":
                queryset = queryset.filter(assignees=self.request.user)
            if team:
                queryset = queryset.filter(assignees__team__name=team)
            if status:
                queryset = queryset.filter(is_completed=status)
            if priority:
                queryset = queryset.filter(priority=priority)

        return queryset.distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm(self.request.GET)
        return context


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "taskmanager/create_task.html"
    success_url = reverse_lazy("taskmanager:tasks")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "taskmanager/create_task.html"
    success_url = reverse_lazy("taskmanager:tasks")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "taskmanager/task_confirm_delete.html"
    success_url = reverse_lazy("taskmanager:tasks")


class TaskCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404("Task does not exist")

        task.is_completed = True
        task.save()
        return redirect("taskmanager:tasks")


class TaskUndoView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404("Task does not exist")

        task.is_completed = False
        task.save()
        return redirect("taskmanager:tasks")
