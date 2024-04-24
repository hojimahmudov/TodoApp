from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    task = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.task


class Movie(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    rating = models.IntegerField()
    phone = models.CharField(max_length=13)

    uzb_gross = models.IntegerField()
    world_gross = models.IntegerField()

    def __str__(self):
        return self.title
