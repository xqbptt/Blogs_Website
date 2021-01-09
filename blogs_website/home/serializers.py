from rest_framework import serializers
from .models import Bookmark, Timeline
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'title_name', 'url_field','date', 'description','image_field']

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id','name','date_started','bookmarks']