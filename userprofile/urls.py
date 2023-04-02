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
from userprofile import views

urlpatterns = [
    path('user_home/', views.user_home, name='user_home'),

    path('myaddress/', views.myaddress, name='myaddress'),
    path('set_default_address/<int:id>/', views.set_default_address, name='set_default_address'),
    # path('editaddress/<int:id>/', views.editaddress, name='editaddress'),
    path('addshippingaddress/', views.addshippingaddress, name='addshippingaddress'),
    path('editshippingaddress/<int:id>/', views.editshippingaddress, name='editshippingaddress'),
    path('deleteshippingaddress/<int:id>/', views.deleteshippingaddress, name='deleteshippingaddress'),


    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('mywishlist/', views.mywishlist, name='mywishlist'),
    path('myorders/', views.myorders, name='myorders'),

    path('editprofile/', views.editprofile, name='editprofile'),

    path('changepassword/', views.changepassword, name='changepassword'),
]
