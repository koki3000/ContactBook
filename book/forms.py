from django import forms
from django.forms import ModelForm
from .models import Contact


class DateInput(forms.DateInput):
    input_type = 'date'


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'birthday': DateInput(),
        }