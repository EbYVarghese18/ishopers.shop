from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart.models import CartItem
from orders.forms import OrderForm
import datetime
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt

import razorpay

# Create your views here.

def payments(request):
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_li9IyzTZMkKzf6', 'W8yNYk7w8opJlsrJxNtjlZTy'))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture': '1'})
        # order_receipt = 'order_rcptid_11'
        # notes = {'Shipping address': 'Bangalore'}
    
    return render(request, 'checkout_selectpayments.html')


@csrf_exempt
def success(request):
    return render(request, 'success.html')


def checkout_address(request, total = 0, quantity = 0):

    current_user = request.user


    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total/100) # give the tax percentage here instead of 2
    grand_total = total + tax


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #store all the billing information inside order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.country = form.cleaned_data['country']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            #to generate order number
            yr = int(datetime.date.today().strftime('%y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }
            return render(request, 'payments.html', context)
        else:
            return redirect('checkout')               



def checkout_payments(request):
    return render(request, 'checkout_selectaddress.html')

def checkout_placeorder(request):
    return render(request, 'checkout_placeorder.html')