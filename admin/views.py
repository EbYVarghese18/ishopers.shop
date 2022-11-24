from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admin_panel(request):
    return HttpResponse("admin_panel")

def admin_signin(request):
    return render(request, 'admin_signin.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_products(request):
    return render(request, 'admin_products.html')

def admin_users(request):
    return render(request, 'admin_users.html')

def admin_orders(request):
    return render(request, 'admin_orders.html')