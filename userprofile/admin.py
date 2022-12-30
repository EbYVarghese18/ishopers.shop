from django.contrib import admin
from django.utils.html import format_html
from userprofile.models import ShippingAddress
 

# Register your models here.

# class UserProfileAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
#     thumbnail.short_description = 'Profile Picture'
#     list_display= ('thumbnail', 'user', 'city', 'state', 'country')

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display= ('user', 'first_name', 'last_name', 'emailaddress', 'city', 'state', 'country', 'is_default')


# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
