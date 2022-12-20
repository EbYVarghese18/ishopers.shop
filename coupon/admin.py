from django.contrib import admin
from coupon.models import Coupon

# Register your models here.

class CoupenAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']

admin.site.register(Coupon, CoupenAdmin)

