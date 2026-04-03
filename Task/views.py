from django.shortcuts import render
from .models import Task
from django.views import generic


class TaskView(generic.ListView):
    model = Task
    template_name = "list.html"
    context_object_name = "tasks"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "detail.html"
    context_object_name = "task"

class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "create.html"
    fields = ["title", "description", "category"]


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "update.html"
    fields = ["title", "description", "category"]

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "delete.html"
    context_object_name = "task"
    success_url = "/"

