from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'orderemail', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'order_note']


class OrderFormStatus(forms.ModelForm):
    class Meta:
        model=Order

        fields=['order_number', 'order_total', 'status']
        
    def __init__(self,*args,**kwargs):
        super(OrderFormStatus,self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control col-6'
            self.fields[field].widget.attrs['readonly'] = True