from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('discover', views.discover),
    path('journey/<name>', views.timeline, name='timeline'),
]
