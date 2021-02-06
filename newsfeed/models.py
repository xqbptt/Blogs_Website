from django.db import models
from accounts.models import User
from django.contrib import auth
from django.utils.timezone import now
from django.utils import timezone
from taggit.managers import TaggableManager


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts1")
    body = models.TextField()
    created_at = models.DateTimeField(default=now)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments1")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)




