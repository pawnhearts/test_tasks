from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description", blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Hint(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    hint = models.TextField("Hint", blank=True)
