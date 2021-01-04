from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
<<<<<<< HEAD
from home.models import User
# Create your views here.

def index(request):
    allPosts = User.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'base.html',context)

def input(request):
    allPosts = User.objects.all()
    context1 = {'allPosts': allPosts}

    if request.method == 'POST':
        url_field = request.POST.get('url')
        context = User(url_field=url_field)
        context.save()

    return render(request, 'input.html',context1)
=======
from home.models import *
from home.Scraper import scraper
from home.Scraper import discoverScraper
from taggit.managers import TaggableManager
import requests
# Create your views here.

def index(request):
    allBookmarks = Bookmark.objects.all()
    context1 = {'allBookmarks': allBookmarks}
    if request.method == 'POST':
        url_field = request.POST.get('url')
        scrap = scraper(url_field)
        bookmark = Bookmark.objects.create(url_field=url_field, title_name = scrap.title, description=scrap.description , image_field=scrap.imgsrc)
        user = request.user
        for tag in scrap.tags:
            bookmark.tags.add(tag)
        bookmark.save()
    return render(request, 'base.html',context1)

def discover(request):
    allBookmarks = Bookmark.objects.all()
    allDiscoverBookmarks = DiscoverBookmark.objects.all()
    context2 = {'allDiscoverBookmarks' : allDiscoverBookmarks}
    return render(request, 'discover.html', context2)

def timeline(request, name):
    curr_timeline = Timeline.objects.get(name = name)
    allBookmarks = curr_timeline.bookmarks.all().order_by('date')
    context1 = {'allBookmarks': allBookmarks}
    return render(request,'journey.html',context1)
>>>>>>> 500be938e643384534ec23761b5b43a348f7d765
