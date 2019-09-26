from django.urls import path
from .views import (
    SignUpView, 
    ProfileView,
    edit_profile_view,
    delete_user_view,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('delete/', delete_user_view, name='delete_user')
]
