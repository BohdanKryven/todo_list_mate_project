from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_change_status,

    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/manage/<int:pk>/<action>", task_change_status, name="task_change_status"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags//create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
    path("task/create", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]

app_name = "todo"
