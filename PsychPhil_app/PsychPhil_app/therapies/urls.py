from django.urls import path, include

from PsychPhil_app.therapies.views import TherapiesCatalogView, AddTherapyView, TherapyDetails, join_therapy, \
    leave_therapy, EditTherapyView, TherapyDeleteView, ShowTherapistsView

urlpatterns = (
    path('', TherapiesCatalogView.as_view(), name='therapies'),
    path('therapyAdd/', AddTherapyView.as_view(), name='therapy add'),
    path('therapistJoin/<int:pk>/', join_therapy, name='therapist join'),
    path('therapistLeave/<int:pk>/', leave_therapy, name='therapist leave'),
    path('details/<int:pk>/', include([
            path('', TherapyDetails.as_view(), name='details therapy'),
            path('edit/', EditTherapyView.as_view(), name='edit therapy'),
            path('delete/', TherapyDeleteView.as_view(), name='delete therapy'),
            path('therapists/', ShowTherapistsView.as_view(), name='show therapists'),
        ])),
)
