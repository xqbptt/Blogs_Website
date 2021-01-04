from . import views
from django.urls import path
from .views import delete_view

urlpatterns = [
    path('', views.index),
    path('discover', views.discover),
    path('<id>/delete', delete_view ),
]
