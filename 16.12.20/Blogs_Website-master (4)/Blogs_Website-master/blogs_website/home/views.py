from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from home.Scraper import scraper
from home.models import *
from home.Scraper import discoverScraper
from taggit.managers import TaggableManager
from django.contrib.auth.decorators import login_required
import requests
from django.db import IntegrityError
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
