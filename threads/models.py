from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

class Thread(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=512)
    pub_date = models.DateTimeField(default=timezone.now)
    points = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=256)
    pub_date = models.DateTimeField(default=timezone.now)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
