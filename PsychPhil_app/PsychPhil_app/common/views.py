from django.views import generic as views
from django.shortcuts import render


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Template view'}  # static context

