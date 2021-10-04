from django.db import models

# Create your models here.
class BroadcastNotification(models.Model):
    message = models.TextField()
    broadcast_on = models.DateFieldField()
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-broadcast_on']