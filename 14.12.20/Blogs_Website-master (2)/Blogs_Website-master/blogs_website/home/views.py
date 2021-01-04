from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from home.models import Bookmark
from home.models import DiscoverBookmark
from home.Scraper import scraper
from home.Scraper import discoverScraper
from taggit.managers import TaggableManager
import requests
# Create your views here.

def login(request):
    return render(request, 'login.html')

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

#def input(request):
  #  allBookmarks = Bookmark.objects.all()
  #  context = {'allBookmarks': allBookmarks}
  #  if request.method == 'POST':
   #     url_field = request.POST.get('url')
   #     context = User(url_field=url_field)
   #     context.save()

    #return render(request, 'input.html',context1)