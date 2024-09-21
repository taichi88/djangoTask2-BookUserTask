
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'author_surname', 'page_num', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author first name'}),
            'author_surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author last name'}),
            'page_num': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of pages'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter book description'}),
        }
