from django.urls import path

from PsychPhil_app.therapies.views import TherapiesCatalogView, AddTherapyView

urlpatterns = (
    path('', TherapiesCatalogView.as_view(), name='therapies'),
    path('therapyAdd/', AddTherapyView.as_view(), name='therapy add'),
)
