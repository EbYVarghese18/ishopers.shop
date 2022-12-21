from django.contrib import admin
from coupon.models import Coupon

# Register your models here.

class CoupenAdmin(admin.ModelAdmin):
    list_display = ['coupon_code', 'is_expired', 'discount', 'minimum_amout']

admin.site.register(Coupon, CoupenAdmin)

