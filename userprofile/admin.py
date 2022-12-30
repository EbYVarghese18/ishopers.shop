from django.contrib import admin
from django.utils.html import format_html
from userprofile.models import ShippingAddress
 

# Register your models here.

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display= ('user', 'first_name', 'last_name', 'emailaddress', 'city', 'state', 'country', 'is_default')


admin.site.register(ShippingAddress, ShippingAddressAdmin)
