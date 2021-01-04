from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
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