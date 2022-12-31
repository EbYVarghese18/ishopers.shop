from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

# Create your views here.

def home(request):
    return render(request, 'home.html')