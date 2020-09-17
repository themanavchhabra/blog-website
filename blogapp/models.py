from django.db import models
from django.urls import reverse
#from froala_editor.fields import FroalaField

# Create your models here.

class Blogpost(models.Model):
    blogtitle = models.CharField(max_length = 100 , unique=False)
    blogcontent = models.TextField(unique=True)
    blogname = models.CharField(max_length = 100, unique=False, null=True)
    blogcreated_on = models.DateTimeField(auto_now_add=True, null=True)
    blogslug = models.SlugField(max_length=200, unique=True, null=True)
    blogtype = models.CharField(max_length=20, unique=False, null=True)
    #blogeditcontent = models.FroalaField(null=True)


class Meta:
    ordering = ['-blogcreated_on']

def __str__(self):
    return self.title

