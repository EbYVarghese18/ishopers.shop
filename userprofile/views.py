from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from orders.models import Order
from userprofile.forms import UserForm, UserProfileForm
from django.contrib import messages
from userprofile.models import UserProfile

# Create your views here.

def user_home(request):
    return render(request, 'userhome.html')


def myaddress(request):
    return render(request, 'myaddress.html')


def mywishlist(request):
    return render(request, 'mywishlist.html')


def myorders(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    context = {
        'orders_count': orders_count,
        'orders': orders,
    }
    # orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    return render(request, 'myorders.html', context)


def editprofile(request):

    userprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('editprofile') 
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'editprofile.html', context)

 