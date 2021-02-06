from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from bookmarksection.models import Bookmark
from accounts.models import User

# Create your models here.
class Timeline(models.Model):
    name = models.CharField(default="No Title",max_length = 264)
    date_started = models.DateTimeField(default = timezone.now)
    bookmarks = models.ManyToManyField(Bookmark)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)