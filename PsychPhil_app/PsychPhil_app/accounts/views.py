from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from PsychPhil_app.accounts.forms import UserCreateForm


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')