from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tag")
    template_name = "todo/index.html"
    ordering = ["status", "-time_created"]


# class TaskCreateView(generic.CreateView):
#     model = Task
#     fields = "__all__"
#     success_url = reverse("todo:index")
#
#
# class TaskUpdateView(generic.UpdateView):
#     model = Task
#     fields = "__all__"
#     success_url = reverse("todo:index")


# class TaskDeleteView(generic.DeleteView):
#     model = Task
#     success_url = reverse("taxi:task-list")
#     template_name = "todo/index.html"


# class TagListView(generic.ListView):
#     model = Tag


# class TagCreateView(generic.CreateView):
#     model = Tag
#     fields = "__all__"
#     success_url = reverse("todo:tag_list")
#
#
# class TegUpdateView(generic.UpdateView):
#     model = Tag
#     fields = "__all__"
#     success_url = reverse("todo:tag_list")


# class TegDeleteView(generic.DeleteView):
#     model = Tag
#     success_url = reverse("taxi:task-list")
#     template_name = "todo/tag_confirm_delete.html"


def task_change_status(request, pk, action):
    task = Task.objects.get(pk=pk)

    if action == "success":
        task.status = True
    if action == "undo":
        task.status = False

    task.save()

    return HttpResponseRedirect(reverse_lazy("todo:index"))
