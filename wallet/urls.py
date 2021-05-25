from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('wallet/', views.user_wallet, name='wallet'),
    path('transaction/', views.user_transactions, name='transaction'),
    path('electricity_bill/', views.ElectricityBill, name='electricity_bill'),
    path('mobile_recharge/', views.MobileRecharge, name='mobile_recharge'),
    path('broadband/', views.Broadband, name='broadband'),
    path('DTH/', views.DTH, name='DTH'),
    path('fast_tag/', views.FastTag, name='fast_tag'),
    path('water/', views.Water, name='water'),

]
