# your_app/context_processors.py

def user_info(request):
    return {
        'is_staff': request.user.is_staff,
        'is_authenticated': request.user.is_authenticated,
    }
