from .views import *
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product
from . import GenericViews as gv
from . import forms

class ProductsList(gv.BaseListView,LoginRequiredMixin,UserPassesTestMixin):
    model = Product
    template_name = 'dashboard/list.html'
    create_url = 'dash:create_product'
    delete_url = 'dash:delete_product'
    fields = [
        (_('Product Image'), 'product_image'),
        (_('Product Name'), 'product_name'),
        (_('Product Quantity'), 'product_quantity'),
        (_('Creation Date'), 'date_added'),
        
        
    ]
    names = [_('Product Name')]
    title = _('Products List')
    
    def test_func(self) :
        user = self.request.user
        return tests.is_staff(user) and tests.is_seller(user)

@login_required
@user_passes_test(tests.is_staff)
def ProductCreate(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return JsonResponse({'status': 'success', 'product_id': product.id})
        else:
            # Collect error messages
            errors = {field: list(errors) for field, errors in form.errors.items()}
            return JsonResponse({'status': 'error', 'errors': errors})
    
    form = forms.ProductForm()  # For GET request
    return render(request, 'dashboard/products/create.html', {'form': form})


class ProductDelete(gv.BaseDeleteView,LoginRequiredMixin):
    model = Product