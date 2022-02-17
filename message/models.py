from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=20)
    message = models.TextField(max_length=120, default="Hi") 