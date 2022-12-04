from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.decorators.cache import cache_control
from .models import Account
from .forms import RegistrationForm


# Create your views here.

# user side starts

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
        return render(request, 'admin_home.html')
    else:
        return redirect('admin_signin')


def admin_orders(request):
    return render(request, 'admin_orders.html')


def admin_products(request):
    return render(request, 'admin_products.html')


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
    return render(request, 'admin_categories.html')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def adduser(request):
#     if 'adminsession' in request.session:
#         if request.method == 'POST':
#             first_name = request.POST['firstname']
#             last_name = request.POST['lastname']
#             user_name = request.POST['username']
#             email = request.POST['email']
#             password = request.POST['password']
#             if User.objects.filter(username=user_name).exists():
#                 messages.info(request, 'Username Taken !')
#                 return redirect('adduser')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Taken !')
#                 return redirect('adduser')
#             else:
#                 user = User.objects.create_user(
#                     first_name=first_name, last_name=last_name, username=user_name, password=password, email=email)
#                 user.save()
#                 messages.success(request, 'The user created succesfully')
#                 return redirect('adminhome')
#         else:
#             return render(request, 'admin_adduser.html')
#     else:
#         return redirect('adminsignin')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def deleteuser(request, username):
#     if 'usersession' in request.session:
#         try:
#             del request.session['usersession']
#         except KeyError:
#             pass
#     try:
#         u = User.objects.get(username=username)
#         u.delete()
#         messages.success(request, "The user is deleted")
#         return redirect('adminhome')
#     except:
#         pass

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def edituser(request, id):
#     if 'adminsession' in request.session:
#         if request.method == 'POST':
#             firstname = request.POST['firstname']
#             lastname = request.POST['lastname']
#             username = request.POST['username']
#             email = request.POST['email']
#             updateuser = User.objects.get(id=id)
#             updateuser.first_name = firstname
#             updateuser.last_name = lastname
#             updateuser.username = username
#             updateuser.email = email
#             updateuser.save()
#             messages.success(request, "User updated successfully")
#             return redirect('adminhome')
#         else:
#             user = User.objects.get(id=id)
#             args = {
#                 'users': user
#             }
#             return render(request, "admin_edituser.html", args)
#     else:
#         return redirect('adminsignin')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def searchuser(request):
#     if 'adminsession' in request.session:
#         username = request.GET['searchuser']
#         searchuser = User.objects.filter(username__icontains=username)
#         return render(request, "admin_searchuser.html", {
#             'users': searchuser
#         })
#     else:
#         return render(request, 'adminsignin.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_signout(request):
    if 'adminsession' in request.session:
        try:
            del request.session['adminsession']
            return redirect('admin_signin')
        except KeyError:
            pass
