from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostUpdateView,
    BlogPostDetailView,
    BlogPostDeleteView,
    BlogPostCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', 
         BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('<int:pk>/', 
         BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('<int:pk>/delete/', 
         BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('new/', BlogPostCreateView.as_view(), name='blogpost_new'),
    path('', BlogPostListView.as_view(), name='blogpost_list'),
]