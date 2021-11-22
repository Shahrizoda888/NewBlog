from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from froala_editor.fields import FroalaField
from .helpers import *


#blog
class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content=FroalaField()
    slug=models.SlugField(max_length=1000, null=True,blank=True)
    image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
