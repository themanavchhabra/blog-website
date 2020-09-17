from django.urls import path
from . import views
from .views import BlogListView, ArticleDetailView, StoryListView, PoemListView, ArticleListView, ExperienceListView

urlpatterns = [
    path('',BlogListView.as_view(),name='homepage'),
    path('blog/<slug:blogslug>',ArticleDetailView.as_view(),name='blogpage'),
    path('create',views.create,name='createpage'),
    path('poems',PoemListView.as_view(),name='poempage'),
    path('stories',StoryListView.as_view(),name='storypage'),
    path('articles',ArticleListView.as_view(),name='articlepage'),
    path('experiences',ExperienceListView.as_view(),name='experiencepage'),
]