from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
from django.utils.html import escape
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from .models import Blogpost

# Create your views here.

blogpost = Blogpost()


class BlogListView(ListView):
    model = Blogpost
    queryset = Blogpost.objects.order_by('-blogcreated_on')
    template_name = 'bloglist.html'

class ArticleDetailView(DetailView):
    model = Blogpost 
    template_name = 'blogpost.html'
    slug_field = 'blogslug'
    slug_url_kwarg = 'blogslug'

class PoemListView(ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(blogtype="poem").order_by('-blogcreated_on')
    template_name = 'filterbloglist.html'

class StoryListView(ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(blogtype="story").order_by('-blogcreated_on')
    template_name = 'filterbloglist.html'

class ArticleListView(ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(blogtype="article").order_by('-blogcreated_on')
    template_name = 'filterbloglist.html'

class ExperienceListView(ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(blogtype="experience").order_by('-blogcreated_on')
    template_name = 'filterbloglist.html'

def create(request):
    global blogpost
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        name = request.POST['name'] 
        slug = request.POST['slug']
        type = request.POST['type'] 
        #editcontent = request.POST['editcontent']    
                
        blogpost.blogname = name 
        blogpost.blogtitle = title
        blogpost.blogcontent = content
        blogpost.blogslug = slug
        blogpost.blogtype = type
        #blogpost.blogeditcontent = editcontent
        blogpost.save()

        return redirect ('homepage') 
    else:
        return render (request,'create.html')   