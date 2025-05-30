from django.db import models
import datetime
from django.core.exceptions import ValidationError


STATUS_CHOICE = (
    ('todo', 'To Do'),
    ('started', 'Started'),
    ('completed', 'Completed')
)

class tasks(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICE, default = 'todo')
    deadline = models.DateField()

    def clean(self):
        if self.deadline < datetime.date.today():
            raise ValidationError("Date cannot be in the past")
        super().clean()

    def __str__(self):
        return self.title