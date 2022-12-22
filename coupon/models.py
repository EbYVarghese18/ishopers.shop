from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class Coupon(models.Model):
    coupon_code = models.CharField( max_length=50, unique=True)
    is_expired = models.BooleanField(default= False)
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000)])
    minimum_amout = models.IntegerField(default = 999)
    
    # valid_from = models.DateTimeField()
    # valid_to = models.DateTimeField()
    # active = models.BooleanField()

    def __str__(self):
        return self.coupon_code 