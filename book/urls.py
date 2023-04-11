from django.urls import path, reverse_lazy
from . import views
from . models import Contact

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('contact/create/', views.CreateContact.as_view(), name="create-contact"),
    path('contact/<slug:pk>/', views.ContactView.as_view(), name="contact"),
]