from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/" +str( self.id)+ "/"

    class Meta:
        ordering = ["-id"]


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=150,
                              choices = [('pending','Pending'),('done','Done')])
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/" +str( self.id)+ "/"

    class Meta:
        ordering = ["-id"]





