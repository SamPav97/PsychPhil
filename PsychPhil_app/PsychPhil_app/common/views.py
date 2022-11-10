from django.views import generic as views


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'common/home_page.html'

