from django import forms
from django.forms import ModelForm
from .models import registration


class registrationFrom(ModelForm):
    class Meta:
        model = registration
        fields = ('name','address','zip_code','email_address','phone','registered_on',)

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code':forms.TextInput(attrs={'class': 'form-control'}),
            'email_address':forms.EmailInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'registered_on':forms.TextInput(attrs={'class': 'form-control'}),
        }