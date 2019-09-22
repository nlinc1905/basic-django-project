from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostUpdateView,
    BlogPostDetailView,
    BlogPostDeleteView,
    BlogPostCreateView,
)
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('<int:pk>/', 
         BlogPostDetailView.as_view(), name='blogpost_detail'),
     path(
        '<int:pk>/edit/', 
        staff_member_required(BlogPostUpdateView.as_view()), 
        name='blogpost_edit'
    ),
    path(
        '<int:pk>/delete/', 
        staff_member_required(BlogPostDeleteView.as_view()), 
        name='blogpost_delete'
    ),
    path(
        'new/', 
        staff_member_required(BlogPostCreateView.as_view()), 
        name='blogpost_new'
    ),    
]