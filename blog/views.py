from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
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


class BlogPostUpdateView(LoginRequiredMixin, 
                         UserPassesTestMixin,
                         UpdateView):
    model = BlogPost
    fields = ('title', 'body',)
    template_name = 'blogpost_edit.html'
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogPostDeleteView(LoginRequiredMixin, 
                         UserPassesTestMixin, 
                         DeleteView):
    model = BlogPost
    template_name = 'blogpost_delete.html'
    success_url = reverse_lazy('blogpost_list')
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blogpost_new.html'
    fields = ('title', 'body',)
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)