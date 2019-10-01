from django.urls import path
from .views import HelloDashView


urlpatterns = [
    path('hello/', HelloDashView.as_view(), name='hello_dash'),
]