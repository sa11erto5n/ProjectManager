from django import forms
from .models import Product ,Contribution, Report, Earning
from .widgets import ImageUploadWidget
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

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


# Contribution Form
class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['user', 'product','product_price']
        
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),  # Bootstrap 5 select
            'product': forms.Select(attrs={'class': 'form-select'}),  # Bootstrap 5 select
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),

        }
    def __init__(self, *args, **kwargs):
        super(ContributionForm, self).__init__(*args, **kwargs)
        User = get_user_model()
        
        # Filter users based on account_type
        self.fields['user'].queryset = User.objects.filter(account_type='contributer')

# Report Form
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['user', 'product', 'quantity', 'price', 'is_returned', 'is_canceled']
        
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),  # Bootstrap 5 select
            'product': forms.Select(attrs={'class': 'form-select'}),  # Bootstrap 5 select
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),  # Bootstrap 5 number input
            'price': forms.NumberInput(attrs={'class': 'form-control'}),  # Bootstrap 5 number input
            'is_returned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Bootstrap 5 checkbox
            'is_canceled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Bootstrap 5 checkbox
        }
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        User = get_user_model()
        # Filter users based on account_type
        self.fields['user'].queryset = User.objects.filter(account_type='seller')



# Earning Form

class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = ['user', 'earning', 'product']
        labels = {
            'user': _('User'),
            'earning': _('Earned Price'),
            'product': _('Product'),
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'earning': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Enter earned price')}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(EarningForm, self).__init__(*args, **kwargs)
        User = get_user_model()
        # Filter users based on account_type
        self.fields['user'].queryset = User.objects.filter(account_type='contruibuter')
