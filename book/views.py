from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import Contact
from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    

class CreateContact(CreateView):
    
    model = Contact
    fields = '__all__'
    template_name = 'book/contact_create_form.html'
    success_url = reverse_lazy("home")


class UpdateContact(UpdateView):
    model = Contact
    fields = '__all__'
    template_name = 'book/contact_update_form.html'
    success_url = reverse_lazy("home")


class DeleteContact(DeleteView):
    model = Contact
    template_name = 'book/contact_delete_form.html'
    success_url = reverse_lazy("home")