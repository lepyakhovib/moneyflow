from django import forms
from .models import Wallet, Expense, Income

class WalletForm(forms.ModelForm):
    name  = forms.CharField(label="Название")
    balance = forms.DecimalField(label="Баланс", max_value=10000000)

    class Meta:
        model = Wallet
        fields = ['name', 'balance']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-name'}),
            'balance': forms.TextInput(attrs={'class': 'form-balance'}),
        }

class ExpenseForm(forms.ModelForm):
    title  = forms.CharField(label="Название")
    amount = forms.DecimalField (label="Сумма", max_value=10000000)
    category = forms.Select()
    wallet = forms.Select()

    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'wallet']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'amount': forms.TextInput(attrs={'class': 'input-field'}),
            'category': forms.Select(attrs={'class': 'input-field'}),
            'wallet': forms.Select(attrs={'class': 'input-field'}),
        }

class IncomeForm(forms.ModelForm):
    title  = forms.CharField(label="Название")
    amount = forms.DecimalField (label="Сумма", max_value=10000000)
    category = forms.Select()
    wallet = forms.Select()

    class Meta:
        model = Income
        fields = ['title', 'amount', 'category', 'wallet']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'amount': forms.TextInput(attrs={'class': 'input-field'}),
            'category': forms.Select(attrs={'class': 'input-field'}),
            'wallet': forms.Select(attrs={'class': 'input-field'}),
        }