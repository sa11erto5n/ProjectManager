from django import forms
from .models import Product
from .widgets import ImageUploadWidget

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_quantity', 'product_price', 'product_image']
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'product_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'product_image': ImageUploadWidget(attrs={
                'class': 'form-control-file',
            }),
        }
