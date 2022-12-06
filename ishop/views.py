from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'usersession' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('signin')
    
