from django.db import models
from django.contrib.auth.models import User
from board.models import Board


class Pin(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pins")
    link = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to="images/")
    boards = models.ManyToManyField(
        Board, related_name="pins", blank=True)

    def __str__(self):
        return self.title
