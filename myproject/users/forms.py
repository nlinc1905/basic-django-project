from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        """
        This class overrides the default fields 
        for UserCreationForm
        """
        model = CustomUser
        fields = ('username', 'email', 'age',)
    

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        """
        This class overrides the default fields 
        for UserChangeForm
        """
        model = CustomUser
        fields = ('username', 'email', 'age',)
