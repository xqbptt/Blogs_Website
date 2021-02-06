from . import views
from .views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter
 
app_name = 'communities'

urlpatterns = [
    path('community', views.communities, name='community'),
    path('communities/<community_name>', views.communityfeed, name='communityfeed'),
    #path('post/create', PostCreateView.as_view(), name="post-create"),
    path('comment/create/<int:post_id>', create_comment, name="comment-create"),
]    