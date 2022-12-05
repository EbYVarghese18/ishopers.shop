from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
from accounts.models import Account
from accounts.forms import RegistrationForm
from store.models import Products
from category.models import Category


# Create your views here.

# user view starts

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if 'usersession' in request.session:
        return redirect('home')
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
            messages.success(request, 'User created successfully')
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signin(request):
    if 'usersession' in request.session:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_superadmin:
                messages.warning(request, 'Try with user account!')
                return redirect('signin')
            else:
                login(request, user)
                request.session['usersession'] = email  # creating session
                return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return render(request, 'signin.html')

    else:
        return render(request, 'signin.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    if 'usersession' in request.session:
        try:
            del request.session['usersession']
            return redirect('signin')
        except KeyError:
            pass


#
#
# admin view starts
#
#


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_signin(request):
    if 'adminsession' in request.session:
        return redirect('admin_home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_superadmin:
                request.session['adminsession'] = email  # creating session
                return redirect('admin_home')
            else:
                messages.warning(request, 'Try with admin account!')
                return redirect('admin_signin')
        else:
            messages.error(request, 'Invalid credentials!')
            return render(request, 'admin_signin.html')
    else:
        return render(request, 'admin_signin.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_home(request):
    if 'adminsession' in request.session:
        context = {
            'users': Account.objects.all()
        }
        return render(request, 'admin_home.html', context)
    else:
        return redirect('admin_signin')


def admin_orders(request):
    return render(request, 'admin_orders.html')
    


def admin_products(request):
    if 'adminsession' in request.session:
        context = {
            'products': Products.objects.all()
        }
        return render(request, 'admin_products.html', context)
    else:
        return redirect('admin_signin')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_users(request):
    if 'adminsession' in request.session:
        args = {
            'users': Account.objects.all()
        }
        return render(request, 'admin_users.html', args)
    else:
        return redirect('admin_signin')



def admin_categories(request):
    if 'adminsession' in request.session:
        context = {
            'categories': Category.objects.all()
        }
        return render(request, 'admin_categories.html', context)
    else:
        return redirect('admin_signin')
    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_signout(request):
    if 'adminsession' in request.session:
        try:
            del request.session['adminsession']
            return redirect('admin_signin')
        except KeyError:
            pass
