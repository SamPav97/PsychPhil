from django.urls import path

from PsychPhil_app.accounts.views import SignInView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
)
