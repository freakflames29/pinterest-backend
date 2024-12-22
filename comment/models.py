from django.db import models
from django.contrib.auth.models import User
from pin.models import Pin


class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return  self.body