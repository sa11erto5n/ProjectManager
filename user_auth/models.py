from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        if not email and not phone_number:
            raise ValueError(_("The Email or Phone number field must be set"))
        
        if email:
            email = self.normalize_email(email)
        
        if phone_number is not None:
            if not isinstance(phone_number, int) or len(phone_number) != 10:
                raise ValueError(_("Phone number should be an integer of length 10"))

        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email=None, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('account_type','admin')
        print(f"Extra Fields: {extra_fields}")  # Debugging output

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email=email, phone_number=phone_number, password=password, **extra_fields)

class User(AbstractUser):
    username = None  # Remove username field
    phone_number = models.CharField(max_length=10, unique=True, default='')  # New phone number field
    profile_pic = models.ImageField(upload_to='profile_pics/', max_length=1200, blank=True, null=True)
    
    ACCOUNT_TYPE_CHOICES = [
        ('admin', _('Administrator')),
        ('seller', _('Seller')),
        ('contributor', _('Contributor')),
    ]
    
    account_type = models.CharField(
        verbose_name=_('Account Type'),
        max_length=12,
        choices=ACCOUNT_TYPE_CHOICES,
    )
    notifications_count = models.IntegerField(default=0)  # Initialize notifications count
    orders_count = models.IntegerField(default=0)  # Initialize orders count

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']  # Optional email field

    objects = UserManager()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
