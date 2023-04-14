from django import forms
from django.forms import ModelForm
from .models import Contact
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['owner',]
        
        widgets = {
            'birthday': DateInput(),      
        }    