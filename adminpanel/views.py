from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils.text import slugify

from accounts.models import Account

from store.models import Products

from category.models import Category

from orders.models import Order
from orders.forms import OrderFormStatus

from adminpanel.forms import CategoryForm, ProductsForm

# Create your views here.


# admin user views starts


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
def admin_signout(request):
    if 'adminsession' in request.session:
        try:
            del request.session['adminsession']
            return redirect('admin_signin')
        except KeyError:
            pass


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_unblock(request, id):
    if 'adminsession' in request.session:
        try:
            user = Account.objects.get(pk=id)
            user.is_active = True
            user.save()
            # messages.info(request, "The user is unblocked")
            return redirect('admin_users')
        except:
            return redirect('admin_signin')
            

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_block(request, id):
    if 'adminsession' in request.session:
        try:
            user = Account.objects.get(pk=id)
            user.is_active = False
            user.save()
            # messages.info(request, "The user is unblocked")
            # del request.session['usersession']
            return redirect('admin_users')
        except:
            return redirect('admin_signin')
    


# Category view starts


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_categories(request):
    if 'adminsession' in request.session:
        context = {
            'categories': Category.objects.all()
        }
        return render(request, 'admin_categories.html', context)
    else:
        return redirect('admin_signin')


def admin_editcategory(request, id):    
    editcategory = Category.objects.get(pk=id)
    categoryform = CategoryForm(instance=editcategory)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=editcategory)
        if form.is_valid():
            editcategory.slug = slugify(editcategory.category_name)
            form.save()
            return redirect('admin_categories')

    context = {
        'categoryform': categoryform,
        }
    return render(request, "admin_editcategory.html", context)


def admin_deletecategory(request, id):
    deletecategory = Category.objects.get(pk=id)
    deletecategory.delete()
    # messages.info(request, "The category item is deleted")
    return redirect("admin_categories")


def admin_addcategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_categories")

    else:
        categoryform = CategoryForm()
        context = {
            'categoryform': categoryform
            }
        return render(request, "admin_addcategory.html", context)



# Products view starts


def admin_products(request):
    if 'adminsession' in request.session:
        context = {
            'products': Products.objects.all()
        }
        return render(request, 'admin_products.html', context)
    else:
        return redirect('admin_signin')


def admin_addproduct(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_products")
    else:
        productform=ProductsForm()
        context={
            'productform':productform,
            }
        return render(request,"admin_addproduct.html", context)


def admin_editproduct(request, id):    
    editproduct=Products.objects.get(pk=id)
    productform=ProductsForm(instance=editproduct)
    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=editproduct)
        if form.is_valid():
            editproduct.slug=slugify(editproduct.product_name)
            form.save()
            return redirect("admin_products")     
    context={
        'productform':productform,
        }
    return render(request,"admin_editproduct.html",context)


def admin_deleteproduct(requset, id):
    deleteproduct=Products.objects.get(pk=id)
    deleteproduct.delete()
    # messages.info(request, "The product item is deleted")
    return redirect("admin_products")




# Order view starts


def admin_orders(request):
    context = {
            'orders': Order.objects.all()
        }
    return render(request, 'admin_orders.html', context)



def orderstatus(request, order_number):
    order=Order.objects.get(order_number=order_number)
    orderform=OrderFormStatus(instance=order)

    if request.method == 'POST':
        form = OrderFormStatus(request.POST,instance=order)
        
        if form.is_valid():
            form.save()
            # messages.info(request, "The order status is updated")
            return redirect('admin_orders')
    else:
        context = {
            'orderform': orderform,
        }
        return render(request, 'orderstatus.html', context)