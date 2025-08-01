from django.urls import path

from .views import (TaskListView,
                    TagListView,
                    TagCreateView,
                    TagUpdateView,
                    TagDeleteView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    complete_task,
                    undo_task)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/complete/", complete_task, name="task-complete"),
    path("task/<int:pk>/undo/", undo_task, name="task-undo"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "task"
