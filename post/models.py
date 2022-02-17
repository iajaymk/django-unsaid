from django.db import models
from django.utils import timezone



class Message(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 