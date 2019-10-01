from django.shortcuts import render
from django.views.generic import TemplateView


class HelloDashView(TemplateView):
    template_name = 'dashboard_templates/hello_dash.html'