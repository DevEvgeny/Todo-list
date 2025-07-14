from django.urls import path

from .views import (TaskListView,
                    TagListView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "task"