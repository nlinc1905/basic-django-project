from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, 
    DeleteView, 
    CreateView
)
from django.urls import reverse_lazy
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'body',)
    template_name = 'blogpost_edit.html'


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost_delete.html'
    success_url = reverse_lazy('blogpost_list')

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogpost_new.html'
    fields = ('title', 'body', 'author',)