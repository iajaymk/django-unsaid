from django.db import models


class Message(models.Model):
    recieverName = models.CharField(max_length = 20, blank = False)
    messageToSend = models.TextField(max_length = 120, blank = False)
    
    def __str__(self):
        return (self.recieverName,self.messageToSend)