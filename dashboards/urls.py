from django.urls import path
from .views import HelloDashView


urlpatterns = [
    path('dashboards/', HelloDashView.as_view(), name='hello_dash'),
]