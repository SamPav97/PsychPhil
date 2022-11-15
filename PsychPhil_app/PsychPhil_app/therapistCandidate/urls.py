from django.urls import path, include

from PsychPhil_app.therapistCandidate.views import CandidateView, acceptance_view

urlpatterns = (
    path('candidate/', CandidateView.as_view(), name='candidate'),
    path('accept/', acceptance_view, name='acceptance'),
)
