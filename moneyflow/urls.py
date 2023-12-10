"""
URL configuration for moneyflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounting.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('wallets/', detail_wallet, name='wallets'),    
    path('wallets/<str:slug>/', view_wallet, name='wallet_url' ),
    path('wallets/<str:slug>/delete/',  deleteWallet, name='delete_wallet'),
    path('wallets/deletexpense/<int:id>/',  deleteExpense, name='delete_expense'),
    path('wallets/deleteincome/<int:id>/',  deleteIncome, name='delete_income'),
    path('create_wallet/', AddWallet.as_view(), name='create_wallet'),
    path('create_expense/', AddExpense.as_view(), name='create_expense'),
    path('create_income/', AddIncome.as_view(), name='create_income')
]
