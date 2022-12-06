from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate
from django.contrib import messages
from accounts.models import Account
from store.models import Products
from django.utils.text import slugify
from category.models import Category
from .forms import CategoryForm, ProductsForm

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