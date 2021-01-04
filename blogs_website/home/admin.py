from django.contrib import admin
<<<<<<< HEAD
from .models import User

# Register your models here.
admin.site.register(User)
=======
from .models import *

# Register your models here.

admin.site.register(Bookmark)
admin.site.register(DiscoverBookmark)
admin.site.register(Timeline)
>>>>>>> 500be938e643384534ec23761b5b43a348f7d765
