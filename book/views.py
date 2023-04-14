from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import Contact
from . forms import ContactForm
from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class HomePageView(LoginRequiredMixin, ListView):
    
    model = Contact

    def get_queryset(self):
        return (
            Contact.objects.filter(owner=self.request.user)
        )
    

class ContactView(LoginRequiredMixin, DetailView):

    model = Contact
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class CreateContact(LoginRequiredMixin, CreateView):
    
    model = Contact
    form_class = ContactForm
    template_name = 'book/contact_create_form.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        data = form.save(commit=False)
        data.owner = self.request.user
        data.save()
        return super(CreateContact, self).form_valid(form)


class UpdateContact(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'book/contact_update_form.html'
    success_url = reverse_lazy("home")


class DeleteContact(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'book/contact_delete_form.html'
    success_url = reverse_lazy("home")