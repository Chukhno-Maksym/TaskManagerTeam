from django.urls import path

from taskmanager.views import (
    index,
    CreateUserView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskDeleteView,
    TaskUpdateView,
    TaskCompleteView,
    TaskUndoView,
)

urlpatterns = [
    path("", index, name="start_page"),
    path("create/", CreateUserView.as_view(), name="create_user"),
    path("user/", UserDetailView.as_view(), name="user_info"),
    path("user/update/", UserUpdateView.as_view(), name="user_update"),
    path("user/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("create_task/", TaskCreateView.as_view(), name="create_task"),
    path("task/<int:pk>", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tasks/<int:pk>/complete", TaskCompleteView.as_view(), name="task_complete"),
    path("tasks/<int:pk>/undo", TaskUndoView.as_view(), name="task_undo"),
]

app_name = "taskmanager"
