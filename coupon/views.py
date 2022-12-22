from django.shortcuts import render, redirect
from coupon.models import Coupon
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart, CartItem

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def coupon_apply(request, total=0, quantity=0, cart_item=None):
    
    appliedcode = request.POST['coupon']

    coupons = Coupon.objects.all()

    try:
        tax = 0
        grand_total = 0
        cart_items = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (18 * total)/100

        for item in coupons:
            if (item.coupon_code == appliedcode):
                total = total - 100
            else:
                pass

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
    return render(request, 'cart.html', context)