from django.urls import path

from PsychPhil_app.therapistCandidate.views import CandidateView, acceptance_view, RefuteCandidate, \
    accept_candidate

urlpatterns = (
    path('candidate/', CandidateView.as_view(), name='candidate'),
    path('accept/', acceptance_view, name='acceptance'),
    path('refute/<int:pk>/', RefuteCandidate.as_view(), name='refute candidate'),
    path('accept/<int:pk>/', accept_candidate, name='accept candidate'),
)
