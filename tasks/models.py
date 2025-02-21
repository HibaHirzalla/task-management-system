from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Task(models.Model):
    # Status choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    # Fields
    title = models.CharField(max_length=100)  # Title with max 100 characters
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')  # User assigned to the task
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')  # User who created the task
    description = models.TextField(blank=True, null=True)  # Optional description
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Status with choices
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the task is created
    due_date = models.DateTimeField(blank=True, null=True)  # Optional due date

    def __str__(self):
        return self.title