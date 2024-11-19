# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

User = get_user_model()


def login_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dash:home')  # Redirect to the dashboard if logged in

    if request.method == "POST":
        identifier = request.POST.get("identifier")
        password = request.POST.get("lpassword")
        # Check if identifier is an email or phone number
        if '@' in identifier:
            user = authenticate(request, email=identifier, password=password)
        else:
            user = authenticate(request, phone_number=identifier, password=password)
        print(user)
        try:
            if user is not None:
                login(request, user)
                return JsonResponse({"success": True, "redirect_url": "dash:home"})
            else:
                return JsonResponse({"success": False, "error": _("Invalid email/phone number or password.")})
        except Exception as e:
                return JsonResponse({"success": False, "error": str(e)})
            
    return render(request, 'auth/log-in.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dash:home')  # Redirect to the dashboard if logged in

    if request.method == "POST":
        email = request.POST.get("semail")
        password = request.POST.get("spassword")
        name = request.POST.get("sname")
        terms = request.POST.get("sterms")

        # Validate input
        errors = {}

        if not email or not email.strip():
            errors['email'] = "Email is required."
        if not password or not password.strip():
            errors['password'] = "Password is required."
        if not name or not name.strip():
            errors['name'] = "Name is required."
        if not terms:
            errors['terms'] = "You must agree to the terms and conditions."

        # Check if email is already in use
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            errors['email'] = "Email is already in use."

        if errors:
            return JsonResponse({"success": False, "errors": errors})

        # Create user if there are no errors
        user = User.objects.create_user(email=email, password=password, first_name=name)
        login(request, user)  # Log the user in after signup

        return JsonResponse({"success": True, "redirect_url": "dash:home"})

    return render(request, 'auth/sign-up.html')
def logout_view(request):
    logout(request)  # Log out the user
    return redirect('frontend:home')  # Redirect to the login page after logging out