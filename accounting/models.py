from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.text import slugify
from random import random
from django.urls import reverse


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10
                                  , decimal_places=2, verbose_name="Баланс")
    name = models.CharField(max_length=255, db_index=True, verbose_name="Название кошелька")
    slug = models.SlugField(max_length=100, unique=True, blank = True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = 'wallet-' + str(slugify(self.name)) + str(random())
        super(Wallet, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('wallet_url', kwargs={'slug': self.slug})    

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'


    @property
    def budget_left(self):
        expense_list = Expense.objects.filter(wallet=self)
        income_list = Income.objects.filter(wallet=self)
        
        total_expense = sum([i.amount for i in expense_list])
        total_income = sum([i.amount for i in income_list]) 
        return self.balance - total_expense + total_income

    @property
    def total_expense(self):
        expense_list = Expense.objects.filter(wallet=self)
        return sum([i.amount for i in expense_list])

    @property
    def total_income(self):
        income_list = Income.objects.filter(wallet=self)
        return sum([i.amount for i in income_list])

    @property
    def total_transactions(self):
        expense_list = Expense.objects.filter(wallet=self)
        income_list = Income.objects.filter(wallet=self)
        return len(expense_list) + len(income_list)
    
    @property
    def len_expense(self):
        return len(Expense.objects.filter(wallet=self))

    @property
    def len_income(self):
        return len(Income.objects.filter(wallet=self))
    
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Expense(models.Model):
    title = models.CharField(max_length=100)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Расход")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return f'{self.title}'


class Income(models.Model):
    title = models.CharField(max_length=100)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Доход")

    class Meta:
        verbose_name = 'Доходы'
        verbose_name_plural = 'Доходы'

    def __str__(self):
        return f'{self.title}'
    

