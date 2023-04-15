from django.urls import path, reverse_lazy
from . import views
from . models import Contact

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('contact/create/', views.CreateContact.as_view(), name="create-contact"),
    path('contact/<int:pk>/update/', views.UpdateContact.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', views.DeleteContact.as_view(), name='contact-delete'),
    path('contact/<int:pk>/', views.ContactView.as_view(), name="contact"),
    path('user/create/', views.CreateUser.as_view(), name="create-user"),
]