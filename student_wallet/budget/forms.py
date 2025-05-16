from django import forms
from .models import Category, Transaction

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'budget_limit']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'description', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
        }