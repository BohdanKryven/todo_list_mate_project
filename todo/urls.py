from django.urls import path

from .views import (
    TaskListView,
    task_change_status,
    # TagListView,
    # TagCreateView,
    # TegUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/manage/<int:pk>/<action>", task_change_status, name="task_change_status"),
    # path("tags/", TagListView.as_view(), name="tag_list"),
    # path("tags//create/", TagCreateView.as_view(), name="tag_create"),
    # path("tags/<int:pk>/update/", TegUpdateView.as_view(), name="tag_update"),
    # path("/<int:pk>/delete/", To_doDeleteView.as_view(), name="to_do-delete"),
    # path("tegs/", TegListView.as_view(), name="tegs-list"),
    # path("tegs/create/", TegCreateView.as_view(), name="teg-create"),
    # path("tegs/<int:pk>/update/", TegUpdateView.as_view(), name="teg-update"),
    # path("tegs/<int:pk>/delete/", TegDeleteView.as_view(), name="teg-delete"),
    ]


app_name = "todo"
