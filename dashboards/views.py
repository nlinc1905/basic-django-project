from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HelloDashView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard_templates/hello_dash.html'
    login_url = 'login'