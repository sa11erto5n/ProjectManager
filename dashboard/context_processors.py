# your_app/context_processors.py
from .models import Request  # Import the Request model
from .models import NotificationsCounter, Request
from django.contrib.auth import get_user_model


def user_info(request):
    return {
        'is_staff': request.user.is_staff,
        'is_authenticated': request.user.is_authenticated,
    }



def global_context(request):
    # Get or create the notifications count (only one entry is expected)
    admin = get_user_model().objects.filter(is_superuser=True,is_staff=True).first()
    
    return {
        'notifications_count': admin.notifications_count,  # Use the stored count
        'orders_count': admin.orders_count,
    }
