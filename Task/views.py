from django.shortcuts import render
from .models import Tasks
from django.views import generic


class TasksView(generic.ListView):
    model = Tasks
    template_name = "list.html"
    context_object_name = "tasks"


class TaskDetailView(generic.DetailView):
    model = Tasks
    template_name = "detail.html"
    context_object_name = "task"

class TaskCreateView(generic.CreateView):
    model = Tasks
    template_name = "create.html"
    fields = ["title", "description", "category"]


class TaskUpdateView(generic.UpdateView):
    model = Tasks
    template_name = "update.html"
    fields = ["title", "description", "category"]

class TaskDeleteView(generic.DeleteView):
    model = Tasks
    template_name = "delete.html"
    context_object_name = "task"
    success_url = "/"
