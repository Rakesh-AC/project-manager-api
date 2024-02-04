from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PriorityChoices(models.TextChoices):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

class StatusChoices(models.TextChoices):
    TODO = "todo"
    IN_PROGRESS = "in progress"
    DONE = "done"

class Project(models.Model):
    title = models.CharField(default="", max_length=100)
    description = models.TextField()
    # created_by = models.ForeignKey(User, null=True, blank=True) 

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateTimeField( auto_now=True, null=True, blank=True)
    priority = models.CharField(default=PriorityChoices.MEDIUM, max_length=50, blank=True)
    status = models.CharField(default=StatusChoices.TODO, max_length=50, blank=True)
    label = models.CharField( max_length=100, null=True, blank=True)
