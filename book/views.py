from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import Contact

# Create your views here.

class HomePageView(ListView):

    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ContactView(DetailView):

    model = Contact
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context