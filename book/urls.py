from django.urls import path, reverse_lazy
from . import views
from . models import Contact
from django.views.generic import CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('contact/<int:pk>/', views.ContactView.as_view(), name="contact"),
    path('contact/create/',
         CreateView.as_view(
            model=Contact,
            fields='__all__',
            success_url=reverse_lazy("home"),
            template_name='book/contact_create_form.html'
         ),
         name='contact-create'),
    path('contact/<int:pk>/update/',
         UpdateView.as_view(
            model=Contact,
            fields='__all__',
            success_url=reverse_lazy("home"),
            template_name='book/contact_update_form.html'
         ),
         name='contact-update'),
    path('contact/<int:pk>/delete/',
         DeleteView.as_view(
            model=Contact,
            success_url=reverse_lazy("home"),
            template_name='book/contact_delete_form.html'
         ),
         name='contact-delete')
]