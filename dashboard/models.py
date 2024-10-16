from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
User = get_user_model()
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db import models

class Product(models.Model):
    product_name        = models.CharField(max_length=100,verbose_name=_('Product Name'))
    product_quantity    = models.IntegerField(verbose_name=_('Product Quantity'))
    product_price       = models.DecimalField(max_digits=10,decimal_places=2)
    product_image       = models.ImageField(upload_to='products/',max_length=1200,verbose_name=_('Product Image'))
    date_added          = models.DateField(auto_now_add=True)