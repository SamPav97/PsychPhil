from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from PsychPhil_app.accounts.models import AppUser
from PsychPhil_app.therapies.forms import CreateTherapy
from PsychPhil_app.therapies.models import Therapy
from PsychPhil_app.therapistCandidate.mixins import TherapistRequiredMixin


class TherapiesCatalogView(views.ListView):
    template_name = 'therapies/therapiesCatalog.html'
    queryset = Therapy.objects.all()
    context_object_name = 'therapies'
    paginate_by = 8


class AddTherapyView(TherapistRequiredMixin, views.CreateView):
    template_name = 'therapies/therapiesAdd.html'
    form_class = CreateTherapy
    success_url = reverse_lazy('therapies')


class TherapyDetails(views.DetailView):
    template_name = 'therapies/therapyDetails.html'
    model = Therapy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #to be owner u gotta have creator in model for theraepy
        context['is_owner'] = self.request.user == self.object
        #get in here is member because u need it for te button join or leave. it might be best to do a therapy style in user and do a relation there insted of many to many in therapy.
        therapy = Therapy.objects.all() \
            .filter(pk=self.object.pk) \
            .get()
        context['is_member_of_therapy'] = self.request.user in therapy.therapists.all()

        #BELOW shows you the user is member of which therpaies. we did this thru a related name in the models. use this when indicating which schools user (current therapist) is member of
        context['therapies_member_of'] = self.request.user.therapists.all()
        print(context['therapies_member_of'])
        if self.request.user.is_authenticated:
            context['is_therapist'] = self.request.user.is_therapist

        return context


def join_therapy(request, pk):
    therapy = Therapy.objects.all()\
               .filter(pk=pk) \
               .get()

    therapy.therapists.add(request.user)

    return redirect('details therapy', pk=pk)


def leave_therapy(request, pk):
    therapy = Therapy.objects.all()\
               .filter(pk=pk) \
               .get()

    therapy.therapists.remove(request.user)

    return redirect('details therapy', pk=pk)
#TODO okay you need to make the join button disappear if alrdy joined and offer leave instead./
#You need to make sure one therapist cannot join other therapies (idk how u gonn do that) maybe at a thing to user that also changes when a therapy is joined
#display all therapists from given therapy and link them to user prof details.