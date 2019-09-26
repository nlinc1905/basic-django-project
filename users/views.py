from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    TemplateView
)
from .forms import (
    CustomUserCreationForm, 
    CustomUserChangeForm,
    DeleteUserForm
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'
    login_url = 'login'


@login_required(login_url='login')
def edit_profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/users/profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_user_profile.html', args)


@login_required(login_url='login')
def delete_user_view(request):
    if request.method == 'POST':
        form = DeleteUserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            request.user.delete()
            return redirect('home')
    else:
        form = DeleteUserForm(instance=request.user)
        args = {'form': form}
        return render(request, 'delete_user.html', args)