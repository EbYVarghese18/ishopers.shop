from django import forms 
from coupon.models import Coupon


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ('coupon_code', 'discount', 'minimum_amout')

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs) 
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control' 