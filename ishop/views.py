from django.shortcuts import render, redirect
from store.models import Products
from django.views.decorators.cache import cache_control
from accounts.models import Account

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'usersession' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('signin')