from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display=('cart_id', 'date_added')

class ClassItemAdmin(admin.ModelAdmin):
    list_display=('product', 'cart', 'quantity')

admin.site.register(Cart, ClassAdmin)
admin.site.register(CartItem, ClassItemAdmin)