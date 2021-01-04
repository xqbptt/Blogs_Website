from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
    path('input', views.input),
]
=======
    path('discover', views.discover),
    path('journey/<name>', views.timeline, name='timeline'),
]
>>>>>>> 500be938e643384534ec23761b5b43a348f7d765
