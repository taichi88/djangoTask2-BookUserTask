

from django import forms
from .models import Reader

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['personal_id', 'name', 'surname', 'email']
        widgets = {
            'personal_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter personal ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
        }
