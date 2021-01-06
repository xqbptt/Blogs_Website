from . import views
from django.urls import path
from home.models import Bookmark

urlpatterns = [
    path('', views.index),
    # path('', views.base),
    # path('blog', views.index),
    path('discover', views.discover),
    path('search', views.search_index),
    path('search/dis', views.search_discover),    
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('journey', views.journey, name='journey'),
    path('journey/<name>', views.timeline, name='timeline'),
    path('addjourney/<int:bookmark_id>', views.addJourney),
    path('addtoexisting/<int:bookmark_id>/<int:timeline_id>', views.addtoexisting),
    path('api/bookmarks/', views.bookmark_list),
    path('api/timelines/', views.timeline_list),
    path('api/bookmark/<int:pk>', views.bookmark_detail),
    path('api/timeline/<int:pk>', views.timeline_detail),
]
