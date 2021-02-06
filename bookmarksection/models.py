from django.db import models
from accounts.models import User
from django.contrib import auth
from django.utils.timezone import now
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.
class Bookmark(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    title_name = models.CharField(default="No Title",max_length = 264)
    url_field = models.URLField(max_length = 200 , unique = True)
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(default="No Description",max_length = 500, null = True)
    image_field = models.URLField(default="none",max_length = 1000)
    tags = TaggableManager()

class DiscoverBookmark(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    title_name = models.CharField(default="No Title",max_length = 264)
    url_field = models.URLField(max_length = 200, unique = True)
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(default="No Description",max_length = 500, null = True)
    image_field = models.URLField(default="none",max_length = 1000)
    tags = TaggableManager()


    
