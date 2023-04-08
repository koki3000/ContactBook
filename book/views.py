from django.shortcuts import HttpResponse, render
from django.views.generic.list import ListView
from . models import Contact

# Create your views here.

class HomePageView(ListView):

    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Contact.objects.all()
        return context