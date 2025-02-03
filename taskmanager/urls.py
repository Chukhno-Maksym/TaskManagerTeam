from django.urls import path, include

from taskmanager.views import (start_page,
                               CreateUserView,
                               TaskListView)

urlpatterns = [
    path("", start_page, name="start_page"),
    path("create/", CreateUserView.as_view(), name="create_user"),
    path("task_list/<str:username>", TaskListView.as_view(), name="task_list"),
]

app_name = "taskmanager"