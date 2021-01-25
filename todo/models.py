from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    activity = models.CharField(max_length=500, help_text="Enter the activity to do.")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    priority_status = (
        ('h', 'High'),
        ('m', 'Medium'),
        ('l', 'Low')
    )

    priority = models.CharField(max_length=1,
                                choices=priority_status,
                                blank=False,
                                default='m',
                                help_text="Priority Status"
                                )

    def get_absolute_url(self):
        return reverse('todo-detail', kwargs={'pk' : self.pk})


    def __str__(self):
        return f'{self.activity} - (Priority : {self.priority})'

