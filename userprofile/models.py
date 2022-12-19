from django.db import models
from accounts.models import Account

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name
    
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'


class ShippingAddress(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    address_line_1 = models.CharField(blank=False, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=False, max_length=20)
    state = models.CharField(blank=False, max_length=20)
    country = models.CharField(blank=False, max_length=20)
    pincode = models.IntegerField(blank=False)
    phone_number = models.BigIntegerField(blank=False)
    is_default = models.BooleanField(default=False)