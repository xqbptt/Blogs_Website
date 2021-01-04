from . import views
from django.urls import path

urlpatterns = [
    path('', views.login),
    path('blog', views.index),
    path('discover', views.discover),
]
