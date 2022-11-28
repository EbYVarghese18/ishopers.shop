from django.shortcuts import render
from store.models import Products

# Create your views here.

def store(request):
    products = Products.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'store.html', context)

def index(request):
    return render(request, 'index.html')