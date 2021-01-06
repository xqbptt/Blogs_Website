from django.contrib import admin
from .models import Bookmark
from .models import DiscoverBookmark
from .models import Timeline

# Register your models here.

admin.site.register(Bookmark)
admin.site.register(DiscoverBookmark)
admin.site.register(Timeline)
