from django import forms

from category.models import Category
from store.models import Products

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

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['product_name', 'slug', 'description', 'price', 'stock', 'is_available', 'category']
    def __init__(self,*args,**kwargs):
        super(ProductsForm,self).__init__(*args,**kwargs)
        self.fields['product_name'].widget.attrs['placeholder']='Enter Product Name' 
        self.fields['slug'].widget.attrs['placeholder']='Enter Product slug'
        self.fields['description'].widget.attrs['placeholder']='Enter Product Description'
        self.fields['price'].widget.attrs['placeholder']='Enter Product price'
        # self.fields['images'].widget.attrs['placeholder']='Enter Product Description'
        self.fields['stock'].widget.attrs['placeholder']='Enter Product stock'
        self.fields['is_available'].widget.attrs['placeholder']='Enter Product is_available'
        self.fields['category'].widget.attrs['placeholder']='Enter Product category'
    
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'