from django.shortcuts import render
from django.views import generic as views

from PsychPhil_app.therapies.models import Therapy


class TherapiesCatalogView(views.ListView):
    template_name = 'therapies/therapiesCatalog.html'
    queryset = Therapy.objects.all()
    context_object_name = 'therapies'
    paginate_by = 3
