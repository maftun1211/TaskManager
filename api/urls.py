from django.urls import path
from .views import CategoryView, TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework.routers import SimpleRouter

app_name = "api"
urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = SimpleRouter()
router.register('categories', CategoryView, basename='category')
urlpatterns += router.urls