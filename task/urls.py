from django.urls import path

from .views import (TaskListView,
                    TagListView,
                    TaskCreateView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "task"