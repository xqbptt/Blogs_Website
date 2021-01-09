from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse,Http404
from django.views.generic import TemplateView
from home.Scraper import scraper
from home.models import *
from home.Scraper import discoverScraper
from taggit.managers import TaggableManager
from django.contrib.auth.decorators import login_required
import requests
from django.db import IntegrityError
from rest_framework.parsers import JSONParser
from .serializers import BookmarkSerializer,TimelineSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


 
# Create your views here.

def base(request):
    # return render(request,'accounts/signup.html')
    return render(request,'index.html')

def index(request):
    allBookmarks = Bookmark.objects.all()
    allTimelines = Timeline.objects.all()
    context1 = {'allBookmarks': allBookmarks,'allTimelines': allTimelines}
    if request.method == 'POST':
        url_field = request.POST.get('url')
            
        
        scrap = scraper(url_field)
        try:
            bookmark = Bookmark.objects.create(url_field=url_field, title_name = scrap.title, description=scrap.description , image_field=scrap.imgsrc)
        except IntegrityError:
            return render(request, 'index.html',context1)
            
            # return HttpResponse("ERROR: Kumquat already exists!")
        user = request.user
        for tag in scrap.tags:
            bookmark.tags.add(tag)
        bookmark.save()
    return render(request, 'index.html',context1)



def discover(request):
    allBookmarks = Bookmark.objects.all()
    allDiscoverBookmarks = DiscoverBookmark.objects.all()
    context2 = {'allDiscoverBookmarks' : allDiscoverBookmarks}
#    i=0
    # for bookmark in allBookmarks:
    #     if(i>10):
    #         break
    #     i=i+1
    #     j=0
    #     for tag in bookmark.tags.all():
    #         if(j>1):
    #             break
    #         j=j+1
    #         tag = str(tag)
    #         url = ('http://newsapi.org/v2/everything?'
    #                 'q='+ tag +'&'
    #                 'from=2020-12-14&'
    #                 'sortBy=popularity&'
    #                 'apiKey=f8e6fd8e886541e783d160dc60faf44e')
    #         response = requests.get(url)
    #         tag_json = response.json()
    #         k=0
    #         for article in tag_json['articles']:
    #             if(k>20):
    #                 break
    #             scrap = discoverScraper(article)
    #             bookmark =  DiscoverBookmark.objects.create(url_field=scrap.URL, title_name = scrap.title, description=scrap.description , image_field=scrap.imgsrc)
    #             user = request.user
    #             for tag in scrap.tags:
    #                 bookmark.tags.add(tag)
    #             bookmark.save()
    return render(request, 'discover.html', context2)

def search_index(request):
    query = request.GET['query']
    allBookmarks = Bookmark.objects.filter(title_name__icontains=query)
    context3 = {'allBookmarks': allBookmarks}
    return render(request,'search_index.html',context3)

def search_discover(request):
    query = request.GET['query']
    allDiscoverBookmarks = DiscoverBookmark.objects.filter(title_name__icontains=query)
    context4 = {'allDiscoverBookmarks': allDiscoverBookmarks}
    return render(request,'search_discover.html',context4)

def delete_post(request,post_id=None):
    post_to_delete=Bookmark.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect("/")

def addJourney(request,bookmark_id):
    journey_name = request.POST.get('name')
    if len(journey_name)>0:
            
            timeline = Timeline.objects.create(name=journey_name)
            timeline.save()
            curr_bookmark = Bookmark.objects.get(id=bookmark_id)
            timeline.bookmarks.add(curr_bookmark)
    return redirect('/')      

def addtoexisting(request,bookmark_id,timeline_id):
    timeline = get_object_or_404(Timeline,id = timeline_id)
    curr_bookmark = Bookmark.objects.get(id=bookmark_id)
    # bookmark = Bookmark.objects.create(url_field="http://google.com", title_name = "ffw", description="dbhbckh")
    timeline.bookmarks.add(curr_bookmark)
    timeline.save()
    return HttpResponse("gandu " + str(curr_bookmark.id) + " "+ curr_bookmark.title_name)     
    # return redirect('/')     


def journey(request):
    allTimelines = Timeline.objects.all()
    context2 = {'allTimelines' : allTimelines}
    return render(request, 'journey_list.html', context2)
     

def timeline(request, name):
    curr_timeline = Timeline.objects.get(name = name)
    allBookmarks = curr_timeline.bookmarks.all().order_by('date')
    context1 = {'allBookmarks': allBookmarks, 'curr_timeline': curr_timeline}
    return render(request,'journey.html',context1)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    lookup_field = 'pk'
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


    


class BookmarkAPIView(APIView):

    def get(self, request):
        bookmarks = Bookmark.objects.all()
        serializer = BookmarkSerializer(bookmarks, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET', 'POST'])

# def bookmark_list(request):
#     if request.method == 'GET':
#         bookmarks = Bookmark.objects.all()
#         serializer = BookmarkSerializer(bookmarks, many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BookmarkSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def bookmark_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         bookmark = Bookmark.objects.get(pk=pk)
#     except Bookmark.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BookmarkSerializer(bookmark)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
        
#         serializer = BookmarkSerializer(bookmark, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         bookmark.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class BookmarkDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Bookmark.objects.get(pk=pk)
        except Bookmark.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bookmark = self.get_object(pk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bookmark = self.get_object(pk)
        serializer = BookmarkSerializer(bookmark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bookmark = self.get_object(pk)
        bookmark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookmarkViewSet(viewsets.ViewSet):
    def list(self, request):
        bookmarks = Bookmark.objects.all()
        serializer = BookmarkSerializer(bookmarks, many = True)
        return Response(serializer.data)

    def create(self,request):
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Bookmark.objects.all()
        bookmark = get_object_or_404(queryset,pk=pk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    def update(self,request,pk=None):
        bookmark = Bookmark.objects.get(pk=pk)
        serializer = BookmarkSerializer(bookmark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TimelineAPIView(APIView):

    def get(self, request):
        timelines = Timeline.objects.all()
        serializer = TimelineSerializer(timelines, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimelineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TimelineDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Timeline.objects.get(pk=pk)
        except Timeline.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        timeline = self.get_object(pk)
        serializer = TimelineSerializer(timeline)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        timeline = self.get_object(pk)
        serializer = TimelineSerializer(timeline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        timeline = self.get_object(pk)
        timeline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        





