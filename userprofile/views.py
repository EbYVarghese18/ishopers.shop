from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_home(request):
    return render(request, 'userprofile.html')


def myaddress(request):
    return render(request, 'myaddress.html')


def mywishlist(request):
    return render(request, 'mywishlist.html')


def myorders(request):
    return render(request, 'myorders.html')