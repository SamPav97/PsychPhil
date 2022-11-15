from django.urls import path

from PsychPhil_app.accounts.views import SignInView, SignUpView, SignOutView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
)
