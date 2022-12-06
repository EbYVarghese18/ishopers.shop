from django.shortcuts import render, get_object_or_404, redirect
from store.models import Products
from category.models import Category
from cart.views import _cart_id
from django.http import HttpResponse
from cart.models import CartItem
from django.views.decorators.cache import cache_control
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def store(request, category_slug=None):
    if 'usersession' in request.session:
        categories = None
        products = None
        if category_slug != None:
            categories = get_object_or_404(Category, slug = category_slug)
            products = Products.objects.filter(category = categories, is_available=True)
            paginator = Paginator(products, 8)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = products.count()
        else:
            products = Products.objects.all().filter(is_available=True).order_by('id')
            paginator = Paginator(products, 8)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = products.count()
        context = {
            'products': paged_products,
            'product_count': product_count, 
        }
        return render(request, 'store.html', context)
    else:
        return redirect('signin')
    
 
def product_detail(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'product_detail.html', context)


def search(request): 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']   
        if keyword:
            products = Products.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        context ={
            'products': products,
            'product_count': product_count,
        } 
    return render(request, 'store.html', context)


def editproduct(request):
    return render(request, 'admin_editproduct.html')