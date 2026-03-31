from django.urls import  path
from.views import TasksView, TaskCreateView, TaskDeleteView, TaskDetailView, TaskUpdateView

app_name = 'Task'
urlpatterns = [
    path('', TasksView.as_view(), name='list'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
]
