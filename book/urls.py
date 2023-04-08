from django.urls import path
from . import views
from . models import Contact

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
]