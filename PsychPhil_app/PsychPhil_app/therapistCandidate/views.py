from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from PsychPhil_app.accounts.models import AppUser
from PsychPhil_app.therapistCandidate.mixins import NonTherapistRequiredMixin, ApplicationInProcessMixin
from PsychPhil_app.therapistCandidate.models import TherapistCand


class CandidateView(ApplicationInProcessMixin, NonTherapistRequiredMixin, LoginRequiredMixin, views.CreateView):
    template_name = 'candidates/candidate.html'
    model = TherapistCand
    fields = ('motivation',)
    success_url = 'index'

    # What is happening here is that I tell the .save() method to not save anything on the database. This way, we get an
    # instance of the model, but no commitment, and thus, no errors. Once we have the object we can inject the logged
    # user and finally save the object to the database, which can happen with no errors.
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# TODO now you have ur sep model for candidate users. once they apply you need a special view where only the super user can see and approve so then once approved the account db needs to become staff
# TODO now whats lefti s to make the applicants is therapist change to true in the account and remove them from applicant list.

# Needs to be function view because I want to use the decorator.
@staff_member_required
def acceptance_view(request):

    candidates = TherapistCand.objects.all()

    context = {
        'candidates': candidates,
    }

    return render(request, 'candidates/admin_view_of_candidates.html', context,)


class RefuteCandidate(views.DeleteView):
    template_name = 'candidates/candidate-refute-page.html'
    model = TherapistCand
    success_url = reverse_lazy('acceptance')



def accept_candidate(request, pk):
    candidate = TherapistCand.objects \
            .filter(pk=pk) \
            .get()

    make_therapist = AppUser.objects \
        .filter(pk=candidate.user_id) \
        .get()
    make_therapist.is_therapist = True
    make_therapist.save()

    candidate.delete()

    return redirect('acceptance')
