from django import forms

from category.models import Category
from store.models import Products
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name', 'slug', 'description']

    def __init__(self,*args,**kwargs):
        super(CategoryForm,self).__init__(*args,**kwargs)
        self.fields['category_name'].widget.attrs['placeholder']='Enter Category Name' 
        self.fields['slug'].widget.attrs['placeholder']='Enter Category slug'
        self.fields['description'].widget.attrs['placeholder']='Enter Category Description'
        
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data=super(CategoryForm,self).clean()
        categoryname=cleaned_data.get('category_name')   
        slugname=cleaned_data.get('slug')   
             
        if len(categoryname)==0:
            raise forms.ValidationError("Please enter category name")
        if len(slugname)==0:
            raise forms.ValidationError("Please enter slug name")


class ProductsForm(forms.ModelForm):
    images = forms.ImageField(required=False, error_messages={'invalid':('image files only')}, widget=forms.FileInput)
    class Meta:
        model = Products
        fields = ['product_name', 'slug', 'description', 'price', 'images', 'stock', 'category']

    def __init__(self,*args,**kwargs):
        super(ProductsForm,self).__init__(*args,**kwargs)
        self.fields['product_name'].widget.attrs['placeholder']='Enter Product Name' 
        self.fields['slug'].widget.attrs['placeholder']='Enter Product slug'
        self.fields['description'].widget.attrs['placeholder']='Enter Product Description'
        self.fields['price'].widget.attrs['placeholder']='Enter Product price'
        self.fields['images'].widget.attrs['placeholder']='Upload Image'
        self.fields['stock'].widget.attrs['placeholder']='Enter Product stock'
        # self.fields['is_available'].widget.attrs['placeholder']='Enter Product is_available'
        self.fields['category'].widget.attrs['placeholder']='Enter Product category'
    
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

        # self.fields['is_available'].widget.attrs['class']='form-check-input ml-2 mt-1'

    def clean(self):
        cleaned_data=super(ProductsForm,self).clean()
        productname=cleaned_data.get('product_name')
        price=cleaned_data.get('price') 
        stock=cleaned_data.get('stock')
        
        if len(productname)==0:
            raise forms.ValidationError("Please enter Product name")
        if price is None:
            raise forms.ValidationError("Please enter Price")
        if stock is None:
            raise forms.ValidationError("Please enter Stock")
        if price < 0:
            raise forms.ValidationError("The price cannot be negative")
        if stock < 0:
            raise forms.ValidationError("The stock cannot be negative")