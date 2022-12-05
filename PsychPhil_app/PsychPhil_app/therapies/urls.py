from django.urls import path, include

from PsychPhil_app.therapies.views import TherapiesCatalogView, AddTherapyView, TherapyDetails, join_therapy, \
    leave_therapy

urlpatterns = (
    path('', TherapiesCatalogView.as_view(), name='therapies'),
    path('therapyAdd/', AddTherapyView.as_view(), name='therapy add'),
    path('therapistJoin/<int:pk>/', join_therapy, name='therapist join'),
    path('therapistLeave/<int:pk>/', leave_therapy, name='therapist leave'),
    path('details/<int:pk>/', include([
            path('', TherapyDetails.as_view(), name='details therapy'),
            #path('update/', UserUpdateView.as_view(), name='update user'),
            #path('delete/', UserDeleteView.as_view(), name='delete user'),
        ])),
)
