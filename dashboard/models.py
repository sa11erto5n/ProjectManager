from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.db import models
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class Product(models.Model):
    product_name            = models.CharField(max_length=100,verbose_name=_('Product Name'))
    product_quantity        = models.IntegerField(verbose_name=_('Product Quantity'))
    remaining_quantity      = models.IntegerField(verbose_name=_('Remaining Quantity'), default=0)
    product_price           = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    product_image           = models.ImageField(upload_to='products/', max_length=1200, verbose_name=_('Product Image'))
    date_added              = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
class Contribution(models.Model):
    user                    = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='contributions', verbose_name=_('User'))
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='contributed_projects', verbose_name=_('Product'))
    product_price           = models.DecimalField(max_digits=10, decimal_places=2,default=0, verbose_name=_('Contribution Price'))
    date_added              = models.DateField(auto_now_add=True)
    
class Report(models.Model):
    user        = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='reports', verbose_name=_('User Reports'))
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='report', verbose_name=_('Product'))
    quantity    = models.IntegerField(verbose_name=_('Sold Quantity'))
    price       = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    date_added  = models.DateField(verbose_name=_('Date Sold'))
    is_returned = models.BooleanField(default=False,verbose_name=_('Returned Products?'))
    is_canceled = models.BooleanField(default=False,verbose_name=_('Canceled Order?'))
    
    def save(self, *args, **kwargs):
        if self.user.account_tye == 'seller':
            # Check if remaining quantity in product is greater than or equal to the quantity sold
            if self.product.remaining_quantity < self.quantity:
                raise ValidationError(_('The remaining quantity of the product is less than the quantity sold.'))
            else:
                # Update remaining quantity in product
                self.product.remaining_quantity -= self.quantity
                self.product.save()  # Save the updated product
                
                # Now save the report itself
                super().save(*args, **kwargs)
        else:
            raise ValidationError(_('Cant create A report'))


class Earning(models.Model):
    user        = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='earnings', verbose_name=_('User Earnings'))
    earning     = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Earned Price'))
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='earning', verbose_name=_('Product'))
    date_added  = models.DateField(auto_now_add=True, verbose_name=_('Date Added'))
    
    def __str__(self):
        return _('ربح %(earning)s دج على %(product)s') % {
            'earning': self.earning,
            'product': self.product,
        }
    
class Request(models.Model):
    TYPE_CHOICES = [
        ('refund', _('Refund')),
        ('reinvest', _('Reinvest')),
    ]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='requests', verbose_name=_('User'))
    project = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='requests', verbose_name=_('Project'))
    earning = models.ForeignKey(Earning, on_delete=models.CASCADE, related_name='requests', verbose_name=_('Earning'))
    request_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name=_('Request Type'))


    def __str__(self):
        return _('Request by %(user)s for %(project)s - %(request_type)s') % {
            'user': self.user,
            'project': self.project,
            'request_type': self.request_type,
        }
# models.py
from django.db import models

class NotificationsCounter(models.Model):
    count = models.PositiveIntegerField(default=0)  # Store the count of notifications

    def __str__(self):
        return f"Notifications Count: {self.count}"


class JoinRequests(models.Model):
    name = models.CharField(_("Full Name"), max_length=350)
    email = models.EmailField(_("Email Address"), blank=True, null=True)
    phone = models.CharField(_("Phone Number"), max_length=15)
    role = models.CharField(
        _("Role"),
        max_length=20,
        choices=[
            ('contributer', _("Contributor")),
            ('seller', _("Seller")),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.get_role_display()}'
