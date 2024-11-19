from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrPhoneBackend(BaseBackend):
    """
    Custom authentication backend that allows login with either email or phone number.
    """
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)  # Try authenticating by email
        except User.DoesNotExist:
            try:
                user = User.objects.get(phone_number=email)  # Try authenticating by phone number
            except User.DoesNotExist:
                return None  # No user found with that email or phone number

        if user.check_password(password):  # Check the password
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
