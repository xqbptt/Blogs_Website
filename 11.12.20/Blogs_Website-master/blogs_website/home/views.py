from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from home.models import Bookmark
from home.Scraper import scraper
# Create your views here.

def index(request):
    allBookmarks = Bookmark.objects.all()
    context1 = {'allBookmarks': allBookmarks}
    if request.method == 'POST':
        url_field = request.POST.get('url')
        scrap = scraper(url_field)
        context = Bookmark(url_field=url_field, user = request.user, title_name = scrap.title, description=scrap.description , image_field=scrap.imgsrc)
        context.save()
    return render(request, 'base.html',context1)


#def input(request):
  #  allBookmarks = Bookmark.objects.all()
  #  context = {'allBookmarks': allBookmarks}
  #  if request.method == 'POST':
   #     url_field = request.POST.get('url')
   #     context = User(url_field=url_field)
   #     context.save()

    #return render(request, 'input.html',context1)