from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from accounts.forms import RegistrationForm
from cart.models import Cart, CartItem
from cart.views import _cart_id

#useractivation
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

import requests

# Create your views here.

# user view starts

def register(request):
    if request.method == 'POST':    
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            #user activation
            current_site = get_current_site(request)
            mail_subject = 'Plesae activate your account'
            message = render_to_string('accountactivationemail.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Registration Successful. Please verify the Email.')
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)



def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_superadmin:
                messages.warning(request, 'Try with user account!')
                return redirect('signin')
            else:
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()  
                    if is_cart_item_exists:
                        cart_item = CartItem.objects.filter(cart=cart)

                        #getting product variation by cart id
                        product_variation =[]
                        for item in cart_item:
                            variation = item.variations.all()
                            product_variation.append(list(variation))
                        
                        # get the cart item from the user to access his product variation
                        cart_item = CartItem.objects.filter(user=user)
                        ex_var_list = []
                        id = []

                        for item in cart_item:
                            existing_variation = item.variations.all()
                            ex_var_list.append(list(existing_variation))
                            id.append(item.id)

                        for pr in product_variation:
                            if pr in ex_var_list:
                                index = ex_var_list.index(pr)
                                item_id = id[index]
                                item = CartItem.objects.get(id=item_id)
                                item.quantity += 1
                                item.user = user
                                item.save()
                            else:
                                cart_item = CartItem.objects.filter(cart = cart)
                                for item in cart_item:
                                    item.user = user
                                    item.save()
                                    
                except:
                    pass
                login(request, user)
                request.session['usersession'] = email  # creating session
                url = request.META.get('HTTP_REFERER')
                try:
                    query = requests.utils.urlparse(url).query
                    params = dict(x.split('=') for x in query.split('&'))
                    if 'next' in params:
                        nextPage = params['next']
                        return redirect(nextPage)
                except:
                    return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return render(request, 'signin.html')
    
    return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('signin')
  

def activate(request, uidb64, token):
    return HttpResponse('okay')