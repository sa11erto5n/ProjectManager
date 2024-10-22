# your_app/context_processors.py
from .models import Request  # Import the Request model
from .models import NotificationsCounter, Request

def user_info(request):
    return {
        'is_staff': request.user.is_staff,
        'is_authenticated': request.user.is_authenticated,
    }



def global_context(request):
    # Get or create the notifications count (only one entry is expected)
    counter, created = NotificationsCounter.objects.get_or_create(id=1)
    
    notifications = Request.objects.all()  # Get all notifications (requests)

    return {
        'notifications_count': counter.count,  # Use the stored count
        'notifications': notifications,
    }
