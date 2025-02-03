from django.urls import path, include

from taskmanager.views import (start_page,
                               CreateUserView,
                               UserDetailView,
                               UserUpdateView,
                               UserDeleteView,
                               TaskListView,
                               TaskCreateView,
                               TaskDetailView, TaskDeleteView, TaskUpdateView)

urlpatterns = [
    path("", start_page, name="start_page"),
    path("create/", CreateUserView.as_view(), name="create_user"),
    path("personal_info/", UserDetailView.as_view(), name="personal_info"),
    path("personal_info/update/",
         UserUpdateView.as_view(),
         name="personal_info_update"),

    path("personal_info/delete/",
         UserDeleteView.as_view(),
         name="personal_info_delete"),
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("create_task/", TaskCreateView.as_view(), name="create_task"),
    path("task/<int:pk>", TaskDetailView.as_view(), name="task_detail"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<int:pk>", TaskDeleteView.as_view(), name="task_delete"),
]

app_name = "taskmanager"