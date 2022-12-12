from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as mixins
from django.shortcuts import render, redirect
from django.views import generic as views

from PsychPhil_app.accounts.models import Profile
from PsychPhil_app.common.forms import SearchPhotosTherapists
from PsychPhil_app.common.models import ClientContact
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


class TextUs(mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'common/text_us.html'
    model = ClientContact
    fields = ('subject', 'content')
    success_url = 'contact'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


@staff_member_required
def texts_view(request):
    texts = ClientContact.objects.all()

    context = {
        'texts': texts
    }

    return render(request, 'common/texts.html', context,)


def delete_text(request, pk):
    text = ClientContact.objects.all().filter(pk=pk).get()

    text.delete()

    return redirect('texts')
