"""ishop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from orders import views

urlpatterns = [

    path('checkout_selectaddress/', views.checkout_selectaddress, name='checkout_selectaddress'),
    path('checkout_selectpayments/', views.checkout_selectpayments, name='checkout_selectpayments'),
    path('checkout_placeorder/', views.checkout_placeorder, name='checkout_placeorder'),
    path('success/', views.success, name='success'),

]
