from django.urls import path, reverse_lazy
from . import views
from . models import Contact

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('contact/<slug:pk>/', views.ContactView.as_view(), name="contact"),
]