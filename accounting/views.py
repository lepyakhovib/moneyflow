import datetime
from django.shortcuts import  redirect, render

from .models import Wallet, Expense, Category, Income
from django.views.generic import CreateView
from django.http import  HttpResponseRedirect
from django.contrib.auth import logout
from .utils import *
from .forms import WalletForm, ExpenseForm, IncomeForm
from .utils import get_plot


def index(request):
    context = {'menuout': menuout}
    return render(request, 'index.html', context=context)


def detail_wallet(request):
    wallets = Wallet.objects.all()
    return render(request, 'wallets.html', {'wallets': wallets, 'menuout': menuout})

def x_day(data):
    date_amount = {i.created_at:0 for i in data}
    for i in data:
        date_amount[i.created_at] += i.amount
    return date_amount

def view_wallet(request, slug):
    wallets = Wallet.objects.get(slug=slug)
    expenses = Expense.objects.filter(wallet=wallets.__dict__['id'])
    income = Income.objects.filter(wallet=wallets.__dict__['id'])
    inc = [sum([i.amount for i in expenses if expenses]), sum(i.amount for i in income if income)]
    x_date = [f'{i.day}/{i.month}/{i.year}' for i in x_day(expenses).keys()]
    y_amount = [i for i in x_day(expenses).values()]
    context = {
        'menuout': menuout, 
        'wallet': wallets, 
        'expenses': expenses, 
        'income': income, 
        'charts': get_plot(['Расходы', 'Доходы'], inc), 
        'ex_date': get_plot1(x_date, y_amount)
        }
    return render(request, 'detail_wallet.html', context=context )

def deleteWallet(request, slug):
    file = Wallet.objects.get(slug=slug)
    file.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteExpense(request, id):
    file = Expense.objects.get(id=id)
    file.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteIncome(request, id):
    file = Income.objects.get(id=id)
    file.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class AddWallet(CreateView):
    form_class = WalletForm
    template_name = 'create_wallet.html'
    success_url= '/wallets/'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = dict(super().get_context_data(**kwargs))
        context.update({'menuout': menuout})
        return dict(list(context.items()))


class AddExpense(CreateView):
    form_class = ExpenseForm
    template_name = 'create_expense.html'    
    success_url = '/wallets/'
    def get_context_data(self,*, object_list=None, **kwargs):
        context = dict(super().get_context_data(**kwargs))
        context.update({'menuout': menuout})
        return dict(list(context.items()))
    

class AddIncome(CreateView):
    form_class = IncomeForm
    template_name = 'create_income.html'
    success_url= '/wallets/'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = dict(super().get_context_data(**kwargs))
        context.update({'menuout': menuout})
        return dict(list(context.items()))
    
