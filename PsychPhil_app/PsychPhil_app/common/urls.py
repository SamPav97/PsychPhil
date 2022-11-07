from django.urls import path

from PsychPhil_app.common.views import IndexViewWithTemplate

urlpatterns = (
    path('', IndexViewWithTemplate.as_view(), name='index'),
)
