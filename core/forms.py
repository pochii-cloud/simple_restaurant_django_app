from django import forms

from .models import contact


class listform(forms.ModelForm):
    class Meta:
        model = contact
        widgets={
             'name':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
             'feedback':forms.TextInput(attrs={'class':'form-control'}),
        }
        fields = ['name', 'email', 'message']
