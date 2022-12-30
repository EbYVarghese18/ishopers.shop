from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from userprofile.models import UserProfile, ShippingAddress
from userprofile.forms import UserForm, UserProfileForm, ShippingAddressForm

from accounts.models import Account

from orders.models import Order, OrderProduct
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.

def user_home(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'userprofile':userprofile
    } 
    return render(request, 'userhome.html', context)



# Address views

def myaddress(request):
    shippingaddress = ShippingAddress.objects.order_by('id').filter(user=request.user)
    context= {
        'shippingaddress': shippingaddress,
    }
    return render(request, 'myaddress.html',context)


def set_default_address(request, id):
    shippingaddressall = ShippingAddress.objects.filter(user=request.user)
    for item in shippingaddressall:
        item.is_default = False
        item.save()

    shippingaddress = ShippingAddress.objects.get(user=request.user, id=id)
    shippingaddress.is_default = True
    shippingaddress.save()
    messages.success(request, 'Default address changed successfully')
    return redirect('myaddress')


def addshippingaddress(request):
    shipping_address=ShippingAddress(user=request.user)
    form = ShippingAddressForm(instance=shipping_address)
    if request.method == 'POST':    
        form = ShippingAddressForm(request.POST, instance=shipping_address)
        if form.is_valid():
            form.save()
            messages.success(request, "The address added successfully")
            return redirect('myaddress')
    context = {
        'shippingaddressform':form,
        }
    return render(request, 'addshippingaddress.html', context)


def editshippingaddress(request, id):
    shipping_address = ShippingAddress.objects.get(id=id)
    shippingaddressform = ShippingAddressForm(instance=shipping_address)
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=shipping_address)
        if form.is_valid():
            form.save()
            messages.success(request, "Your address has been updated.") 
            return redirect('myaddress') 
    context = {
            'form': shippingaddressform,
        } 
    return render(request, 'editshippingaddress.html', context)

def deleteshippingaddress(request, id):
    shipping_address = ShippingAddress.objects.get(id=id)
    if shipping_address.is_default == True:
        messages.error(request, "The addres is the default one. Please change default address and try again.")
    else:
        shipping_address.delete()
        messages.success(request, "The address is deleted")
    return redirect('myaddress')


def mywishlist(request):
    return render(request, 'mywishlist.html')


@login_required(login_url='signin')
def myorders(request):

    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    
    paginator = Paginator(orders, 10)
    page = request.GET.get('page')
    paged_orders = paginator.get_page(page)

    order_count = orders.count()
    
    context = {
        'orders': paged_orders,
        'order_count': order_count,
        } 
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


@login_required(login_url='signin')
def order_detail(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number = order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_detail:
        subtotal += i.product_price * i.quantity
    context = {
        'order_detail': order_detail,
        'order': order,
        'subtotal': subtotal,
    }
    return render(request, 'order_detail.html', context)
