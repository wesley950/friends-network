from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
