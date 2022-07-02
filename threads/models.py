from django.db import models
from django.utils import timezone

from profiles.models import User

class Thread(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=512)
    pub_date = models.DateTimeField(default=timezone.now)
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

class Upvote(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.username + ' upvoted "' + self.thread.title + '"'
