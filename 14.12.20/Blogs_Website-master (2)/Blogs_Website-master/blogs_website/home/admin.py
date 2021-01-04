from django.contrib import admin
from .models import Bookmark
from .models import DiscoverBookmark

# Register your models here.

admin.site.register(Bookmark)
admin.site.register(DiscoverBookmark)
