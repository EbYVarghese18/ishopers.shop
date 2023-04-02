from django.contrib import admin
from coupon.models import Coupon, UsedCoupons

# Register your models here.

class CoupenAdmin(admin.ModelAdmin):
    list_display = ['coupon_code', 'is_expired', 'discount', 'minimum_amout']

class UsedCouponsAdmin(admin.ModelAdmin):
    list_display = ['coupon_code', 'email']

admin.site.register(Coupon, CoupenAdmin)
admin.site.register(UsedCoupons, UsedCouponsAdmin)