from django.db import models
from accounts.models import User
from django.contrib import auth
from django.utils.timezone import now
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    created_at = models.DateTimeField(default=now)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    content = models.TextField()
    created_at = models.DateTimeField(default=now)


# Create your models here.
class Community(models.Model):
    community_name = models.CharField(default="No Name",max_length = 264)
    description = models.CharField(default="No Description",max_length = 500, null = True)
    members = models.ManyToManyField(User, related_name="members")
    posts = models.ManyToManyField(Post, related_name="community_posts")
    





    