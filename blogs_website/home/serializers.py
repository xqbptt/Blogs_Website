from rest_framework import serializers
from .models import *
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'title_name', 'url_field', 'date', 'description', 'image_field']

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id', 'name', 'date_started', 'bookmarks', 'user' ]