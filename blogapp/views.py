from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from .models import BlogPost
# Create your views here.
class BlogView(ListView):
    model=BlogPost
    context_object_name='posts'
    template_name="Posts/blogView.html"

class BlogCreateWithFields(CreateView):
    model=BlogPost
    fields= ['title','content','author','created_on']
    template_name= "Posts/blogcreate.html"
    success_url=reverse_lazy('Posts:listhtml')

class BlogCreateWithForm(CreateView):
    model=BlogPost
    fields= ['title','content','author','created_on']
    template_name= "Posts/blogCreateForm.html"
    success_url=reverse_lazy('Posts:listhtml')