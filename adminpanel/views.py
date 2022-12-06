from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate
from django.contrib import messages
from accounts.models import Account
from store.models import Products
from category.models import Category

# Create your views here.


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
        user = Account.objects.all()
        args = {
            'users': user,
        }
        return render(request,'admin_users.html', args)
    else:
        return redirect('admin_signin')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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



# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def block_user(request, id):
#     blockuser=Account.objects.get(pk=id)
#     blockuser.is_active=False
#     blockuser.save()
#     return redirect("admin_users")



# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def unblock_user(request, id):
#     unblockuser=Account.objects.get(pk=id)
#     unblockuser.is_active=True
#     unblockuser.save()
#     return redirect("admin_users")