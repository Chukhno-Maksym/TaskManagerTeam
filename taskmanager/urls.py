from django.urls import path, include

from taskmanager.views import index

urlpatterns = [
    path("", index, name="index"),
]
