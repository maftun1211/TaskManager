from rest_framework.serializers import ModelSerializer
from Task.models import Task, Category
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'description','status', 'created_at', 'category']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
