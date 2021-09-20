from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=15, default="User")
    sent_message = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)


# superuser pass = pass1234