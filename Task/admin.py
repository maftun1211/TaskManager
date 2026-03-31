from django.contrib import admin

from api.views import CategoryView
from .models import Tasks


admin.site.register(Tasks, CategoryView)
