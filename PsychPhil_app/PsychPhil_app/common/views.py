
from django.views import generic as views

from PsychPhil_app.therapies.models import Therapy


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
