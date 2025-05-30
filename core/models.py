from django.db import models


STATUS_CHOICE = (
    ('todo'), ('To Do'),
    ('started'), ('Started'),
    ('completed'), ('Completed')
)

class tasks(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_add_now = True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICE, default = 'todo')
    deadline = models.DateField()


    def __str__(self):
        return self.title