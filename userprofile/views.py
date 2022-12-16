from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from accounts.models import Account

from orders.models import Order

from userprofile.models import UserProfile
from userprofile.forms import UserForm, UserProfileForm

# Create your views here.

def user_home(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'userprofile':userprofile
    } 
    return render(request, 'userhome.html', context)


def myaddress(request):
    return render(request, 'myaddress.html')


def mywishlist(request):
    return render(request, 'mywishlist.html')


@login_required(login_url='signin')
def myorders(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    context = {
        'orders_count': orders_count,
        'orders': orders,
    }
    # orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    return render(request, 'myorders.html', context)


@login_required(login_url='signin')
def editprofile(request):
         
    userprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, "Your profile has been updated.") 
            return redirect('user_home') 
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)

    context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'userprofile':userprofile
        } 
    return render(request, 'editprofile.html', context)


@login_required(login_url='signin')
def changepassword(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact = request.user.username)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request)
                messages.success(request, 'Password updated successfully')
                return redirect('changepassword')
            else:
                messages.error(request, 'Please enter a valid current password')
                return redirect('changepassword')
        else:
            messages.error(request, 'Password does not match')
            return redirect('changepassword')
    return render(request, 'changepassword.html')