from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views import generic as views
from PsychPhil_app import settings
from PsychPhil_app.therapistCandidate.mixins import NonTherapistRequiredMixin
from PsychPhil_app.therapistCandidate.models import TherapistCand

UserModel = get_user_model()


class CandidateView(NonTherapistRequiredMixin, LoginRequiredMixin, views.CreateView):
    template_name = 'candidates/candidate.html'
    model = TherapistCand
    fields = ('motivation', 'cv',)
    success_url = 'index'

    # What is happening here is that I tell the .save() method to not save anything on the database. This way, we get an
    # instance of the model, but no commitment, and thus, no errors. Once we have the object we can inject the logged
    # user and finally save the object to the database, which can happen with no errors.
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # I should make exception less broad.
        try:
            is_candidate = TherapistCand.objects.all() \
                .filter(user_id=self.request.user.pk) \
                .get()
            context['is_candidate'] = is_candidate
        except:
            context['is_candidate'] = False

        return context


# Needs to be function view because I want to use the decorator.
@staff_member_required
def acceptance_view(request):
    # Pagination would be nice here.

    candidates = TherapistCand.objects.all()

    context = {
        'candidates': candidates,
    }

    return render(request, 'candidates/admin_view_of_candidates.html', context,)


class RefuteCandidate(views.DeleteView):
    template_name = 'candidates/candidate-decline-page.html'
    model = TherapistCand
    success_url = reverse_lazy('see candidates')


# This is a complicated view. If I accept the candidate I need to delete him from the table with applicants,
# make him a therapist, and also add him to the admin group of therapists.
# Then I send out the email that candidate was accepted. I cannot do this in signal because there is no universal
# event happening to bind the signal to. It is specific only to this view.
def accept_candidate(request, pk):
    candidate = TherapistCand.objects \
            .filter(pk=pk) \
            .get()

    make_therapist = UserModel.objects \
        .filter(pk=candidate.user_id) \
        .get()
    make_therapist.is_therapist = True
    make_therapist.is_staff = True
    make_therapist.save()

    admin_group = Group.objects.first()
    admin_group.user_set.add(make_therapist)

    user = UserModel.objects.all() \
        .filter(pk=candidate.user_id) \
        .get()

    candidate.delete()

    email_content = render_to_string('email_templates/approved_for_therapist.html', {
        'user': user,
    })
    send_mail(
        subject='Your application for therapist was successful!',
        message=strip_tags(email_content),
        html_message=email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(user.email,),
    )

    return redirect('see candidates')
