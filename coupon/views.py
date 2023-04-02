from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from cart.models import Cart, CartItem

from orders.models import Order

from coupon.models import Coupon,UsedCoupons

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def coupon_apply(request, order_number):
    
    appliedcode = request.POST['coupon']
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=order_number)
    
    # saving coupon to order table
    order.coupon = appliedcode
    order.save()

    tax = 0
    grand_total = 0
    cart_items = 0
    total=0
    quantity=0
    cart_item=None
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity= cart_item.quantity    
    tax = (18 * total)/100

    usedcoupon = UsedCoupons.objects.all()
    result = 'canuse'
    for item in usedcoupon:
        if(order.orderemail == item.email) and (appliedcode == item.coupon_code):
            result = 'used'
            break
        else:
            result = 'canuse'

    coupons = Coupon.objects.filter(coupon_code__exact=appliedcode)
    if coupons:
        for i in coupons:
            if(i.is_expired == False):
                if(total >= i.minimum_amout):
                    if(result == 'canuse'): 
                        discount = i.discount
                        grand_total = total + tax - discount
                        order.order_total = grand_total
                        order.save()
                        context = {
                            'total': total,
                            'quantity': quantity,
                            'cart_items': cart_items,
                            'tax': tax,
                            'grand_total': grand_total,
                            'order': order,
                            'appliedcode': appliedcode,
                            'discount': discount,
                        }
                        msg = 'Coupon applied succesfully'
                        return render(request, 'checkout_review.html', context)
                    else:
                        msg = 'Coupon already used'
                else:
                    msg = 'Minimum amount is: '+ str(i.minimum_amout)
            else:
                msg = 'Coupon Expired'
        grand_total = total + tax
        context = {
            'total': total,
            'quantity': quantity,
            'cart_items': cart_items,
            'tax': tax,
            'grand_total': grand_total,
            'order': order,
        }

        messages.info(request, msg)
        return render(request, 'checkout_review.html', context)
    else:
        grand_total = total + tax
        context = {
            'total': total,
            'quantity': quantity,
            'cart_items': cart_items,
            'tax': tax,
            'grand_total': grand_total,
            'order': order,
        }
        messages.error(request, 'Coupon Does not Exist')
        return render(request, 'checkout_review.html', context)