from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from PsychPhil_app.therapies.forms import CreateTherapy, EditTherapy
from PsychPhil_app.therapies.models import Therapy
from PsychPhil_app.therapistCandidate.mixins import TherapistRequiredMixin


class TherapiesCatalogView(views.ListView):
    template_name = 'therapies/therapiesCatalog.html'
    queryset = Therapy.objects.all()
    context_object_name = 'therapies'
    paginate_by = 6


class AddTherapyView(TherapistRequiredMixin, views.CreateView):
    template_name = 'therapies/therapiesAdd.html'
    form_class = CreateTherapy
    success_url = reverse_lazy('therapies')

    # Overwrite form to save current user as creator user.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTherapyView, self).form_valid(form)


class EditTherapyView(TherapistRequiredMixin, views.UpdateView):
    template_name = 'therapies/therapyEdit.html'
    form_class = EditTherapy
    model = Therapy

    def get_success_url(self):
        return reverse_lazy('details therapy', kwargs={
            'pk': self.object.pk,
        })


class TherapyDeleteView(views.DeleteView):
    template_name = 'therapies/therapy delete.html'
    model = Therapy
    success_url = reverse_lazy('therapies')


class TherapyDetails(views.DetailView):
    template_name = 'therapies/therapyDetails.html'
    model = Therapy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get current therapy
        therapy = Therapy.objects.all() \
            .filter(pk=self.object.pk) \
            .get()

        # Check if user is already member of this therapy/school.
        context['is_member_of_therapy'] = self.request.user in therapy.therapists.all()
        context['is_owner'] = self.request.user == therapy.user

        # Below shows which therapies user is member of.
        # This was done through a related name in the models.
        if self.request.user.is_authenticated:
            context['therapies_member_of'] = self.request.user.therapists.all()
        if self.request.user.is_authenticated:
            context['is_therapist'] = self.request.user.is_therapist
        return context


class ShowTherapistsView(views.ListView):
    template_name = 'therapies/therapists.html'
    model = Therapy
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        therapy = Therapy.objects.all() \
            .filter(pk=self.kwargs['pk']) \
            .get()
        context['therapy'] = therapy
        therapists = therapy.therapists.all()
        context['therapists'] = therapists

        return context


# Not sure if those should be in a 'utils' file because I use them
# as functions but not as views:
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
