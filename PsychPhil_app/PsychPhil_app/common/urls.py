from django.urls import path
from PsychPhil_app.common.views import IndexViewWithTemplate, ContactView, AboutView, all_therapists, TextUs, \
    texts_view, delete_text

urlpatterns = (
    path('', IndexViewWithTemplate.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('searchTherapists/', all_therapists, name='search'),
    path('textus/<int:pk>', TextUs.as_view(), name='text us'),
    path('texts/', texts_view, name='texts'),
    path('deleteMessage/<int:pk>', delete_text, name='delete message')
)
