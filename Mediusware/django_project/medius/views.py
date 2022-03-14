# from msilib.schema import File
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'medius/home.html'