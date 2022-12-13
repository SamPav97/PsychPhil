from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views

from PsychPhil_app.accounts.forms import SignUpForm, EditForm
from PsychPhil_app.accounts.models import Profile

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    # Signs the user in, after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['therapies_member_of'] = self.object.therapists.all()

        context['is_owner'] = self.request.user == self.object
        context['is_therapist'] = self.object.is_therapist

        return context


class UserUpdateView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    form_class = EditForm
    model = Profile

    # fields = ('first_name', 'last_name', 'gender', 'age', 'self_summary', 'image')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_therapist'] = self.request.user.is_therapist

        return context

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
