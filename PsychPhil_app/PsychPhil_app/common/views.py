from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

from PsychPhil_app.accounts.models import Profile
from PsychPhil_app.common.forms import SearchPhotosTherapists
from PsychPhil_app.therapies.models import Therapy

UserModel = get_user_model()


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'common/home_page.html'


class ContactView(views.TemplateView):
    template_name = 'common/contact.html'


class AboutView(views.TemplateView):
    template_name = 'common/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['therapies'] = Therapy.objects.all()
        return context


def all_therapists(request):
    search_form = SearchPhotosTherapists(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['therapistName']

    therapists = UserModel.objects.all()\
        .filter(is_therapist=True)

    therapist_details = [therapist for therapist in Profile.objects.all() if therapist.user_id in [therapist.pk for therapist in therapists]]

    if search_pattern:
        therapist_details = Profile.objects.all().filter(last_name__contains=search_pattern)
        therapist_details |= Profile.objects.all().filter(first_name__contains=search_pattern)

    context = {
        'therapists': therapist_details,
        'form': search_form
    }

    return render(
        request,
        'common/search_therapists.html',
        context,
    )