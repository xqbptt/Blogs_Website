from . import views
from django.urls import path,include
from home.models import Bookmark
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bookmark',views.BookmarkViewSet,basename='bookmark')
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
    #path('bookmarks/', views.bookmark_list),
    path('bookmarks/', views.BookmarkAPIView.as_view()),
    #path('bookmarks/<int:pk>/', views.bookmark_detail),
    path('bookmarks/<int:pk>/', views.BookmarkDetail.as_view()),
    path('generic/bookmarks/<int:pk>/', views.GenericAPIView.as_view()),
    path('generic/bookmarks/', views.GenericAPIView.as_view()),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    path('timelines/', views.TimelineAPIView.as_view()),
    path('timelines/<int:pk>/', views.TimelineDetail.as_view()),


]
