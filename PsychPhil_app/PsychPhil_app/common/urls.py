from django.urls import path

from PsychPhil_app.common.views import IndexViewWithTemplate, ContactView, AboutView, all_therapists

urlpatterns = (
    path('', IndexViewWithTemplate.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('searchTherapists/', all_therapists, name='search')
)
