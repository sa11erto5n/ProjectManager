# models.py
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        """Creates and returns a user with an email or phone number and password."""
        if not email and not phone_number:
            raise ValueError("The Email or Phone number field must be set")
        
        if email:
            email = self.normalize_email(email)
        
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    username = None  # Remove username field
    # email = models.EmailField(unique=True, null=True, blank=True)  # Email can be optional
    phone_number = models.CharField(max_length=10, unique=True,default='')  # New phone number field
    profile_pic = models.ImageField(upload_to='profile_pics/', max_length=1200, blank=True, null=True)
    # birthdate = models.DateField(null=True, blank=True)
    ACCOUNT_TYPE_CHOICES = [
        ('seller', _('Seller')),
        ('contributor', _('Contributor')),
    ]

    account_type = models.CharField(
        verbose_name=_('Account Type'),
        max_length=12,
        choices=ACCOUNT_TYPE_CHOICES,default=''
    )
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']  # Optional email field

    objects = UserManager()

    def __str__(self):
        return f' {self.first_name} {self.last_name} '

