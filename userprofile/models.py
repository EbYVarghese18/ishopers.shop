from django.db import models
from accounts.models import Account


class ShippingAddress(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    address_line_1 = models.CharField(blank=False, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    emailaddress = models.EmailField(max_length=50, blank=False)
    city = models.CharField(blank=False, max_length=20)
    state = models.CharField(blank=False, max_length=20)
    country = models.CharField(blank=False, max_length=20)
    pincode = models.IntegerField(blank=False)
    phone_number = models.BigIntegerField(blank=False)
    is_default = models.BooleanField(default=False)