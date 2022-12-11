from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart.models import CartItem, Cart
from cart.views import _cart_id
from orders.forms import OrderForm
import datetime
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import razorpay

# Create your views here.


@login_required(login_url='signin')
def checkout_selectaddress(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
            tax = (2 * total)/100
            grand_total = total + tax
    except ObjectDoesNotExist:
        pass
        
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        }
    return render(request, 'checkout_selectaddress.html', context)



@login_required(login_url='signin')
def checkout_selectpayments(request, total = 0): 
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
    tax = (2 * total/100) # give the tax percentage here instead of 2
    grand_total = total + tax
    context = {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'checkout_selectpayments.html', context)



@login_required(login_url='signin')
def checkout_placeorder(request,total = 0):
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_li9IyzTZMkKzf6', 'W8yNYk7w8opJlsrJxNtjlZTy'))
        payment = client.order.create({
            'amount':amount, 
            'currency':'INR', 
            'payment_capture': '1',
            })
        order_receipt = 'order_rcptid_11'
        notes = {
            'Shipping address': 'Bangalore', 
            }
    else:
        current_user = request.user
        cart_items = CartItem.objects.filter(user=current_user)
        grand_total = 0
        tax = 0
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
        tax = (2 * total/100) # give the tax percentage here instead of 2
        grand_total = total + tax
        context = {
            'cart_items': cart_items,
            'total': total,
            'tax': tax,
            'grand_total': grand_total,
        }
        return render(request, 'checkout_placeorder.html', context)
    


@csrf_exempt
def success(request):
    return render(request, 'success.html')