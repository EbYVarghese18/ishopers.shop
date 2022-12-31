
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ishop import views


urlpatterns = [
        
    path('securelogin/', admin.site.urls),
    
    path('', views.home, name='home'),

    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('accounts.urls')),
    path('adminpanel/', include('adminpanel.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('orders/', include('orders.urls')),
    path('coupon/', include('coupon.urls')),
]  

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)