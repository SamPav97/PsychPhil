from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from PsychPhil_app.therapies.forms import CreateTherapy
from PsychPhil_app.therapies.models import Therapy


class TherapiesCatalogView(views.ListView):
    template_name = 'therapies/therapiesCatalog.html'
    queryset = Therapy.objects.all()
    context_object_name = 'therapies'
    paginate_by = 8


class AddTherapyView(views.CreateView):
    template_name = 'therapies/therapiesAdd.html'
    form_class = CreateTherapy
    success_url = reverse_lazy('therapies')

#TODO make add only for therapists. also make button appear only if therapist