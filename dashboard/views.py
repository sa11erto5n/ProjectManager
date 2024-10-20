from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _
from . import tests
from django.core.exceptions import PermissionDenied


User = get_user_model()

@login_required
def home_view(request):
    print(request.user.is_staff)
    return render(request,'dashboard/index.html')



#======> Users
@staff_member_required
def users_view(request):
    context = {
        'users': get_user_model().objects.all().exclude(is_staff=True),
    }
    return render(request,'dashboard/users.html',context=context)

@login_required
@staff_member_required
@csrf_exempt  # To allow AJAX POST requests
def create_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('p_number')
        account_type = request.POST.get('acc_type')
        password = request.POST.get('user_password')

        errors = {}

        # Validate the inputs
        if not first_name:
            errors['first_name'] = _('First Name is required.')
        if not last_name:
            errors['last_name'] = _('Last Name is required.')
        if not phone_number or len(phone_number) != 10:
            errors['p_number'] = _('Phone number must be 10 digits long.')
        if account_type not in ['seller', 'contributer']:  # Updated to match the template options
            errors['acc_type'] = _('Invalid account type selected.')
        if not password or len(password) < 4:
            errors['user_password'] = _('Password must be at least 4 characters long.')

        # If any errors, return the error response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)

        # If no errors, create the user
        try:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                account_type=account_type,
                password=make_password(password),  # Hash the password
            )
            return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'errors': str(e)}, status=500)

    # For GET requests, render the user creation form
    return render(request, 'dashboard/create_user.html')


@login_required
@user_passes_test(tests.is_staff)
def user_edit(request,id):
    user = User.objects.get(pk=id)
    context= {
        'user' : user
    }
    print(user)
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            # email = request.POST.get('email')  # Email is no longer required
            # birthdate = request.POST.get('birthdate')
            profile_pic = request.FILES.get('profile_pic')
            p_number = request.POST.get('p_number')
            account_type = request.POST.get('acc_type')
            password = request.POST.get('user_password')
            errors = {}
            print(account_type)
            # Validate the inputs
            if not first_name:
                errors['first_name'] = 'First name is required'
            if not last_name:
                errors['last_name'] = 'Last name is required'
            if not p_number:
                errors['p_number'] = 'Phone Number is required'
            elif len(p_number) != 10:
                errors['p_number'] = 'Phone number must be exactly 10 digits.'
            # Email validation (check for duplicates, but not required)
            # if email and get_user_model().objects.filter(email=email).exclude(id=user.id).exists():
            #     errors['email'] = 'This email is already in use by another account.'

            # Phone number validation (check for duplicates)
            if p_number and get_user_model().objects.filter(phone_number=p_number).exclude(id=user.id).exists():
                errors['p_number'] = 'This phone number is already in use by another account.'

            # Handle profile picture validation if an image was uploaded
            if profile_pic:
                # Example of validating image size and format
                if profile_pic.size > 5 * 1024 * 1024:  # Limit file size to 5 MB
                    errors['profile_pic'] = 'Profile picture size should not exceed 5MB.'
                if not profile_pic.content_type.startswith('image/'):
                    errors['profile_pic'] = 'Invalid file format. Please upload an image file.'

            # If there are any errors, send them back to the front-end
            if errors:
                return JsonResponse({'status': 'error', 'errors': errors})

            # Update the user's details
            user.first_name = first_name
            user.last_name = last_name
            # Update email only if provided
            # user.email = email
            # user.birthdate = birthdate
            user.phone_number = p_number  # Update phone number
            user.account_type = account_type
            print(user.account_type)
            if password :
                user.password = make_password(password)

            # Handle profile picture if uploaded
            if profile_pic:
                try:
                    user.profile_pic = profile_pic
                except Exception as e:
                    print(f'Uploading Error : {str(e)}')

            # Save the updated user object
            user.save()
            return JsonResponse({'status': 'success'})

        except Exception as e:
            # Capture any other errors (e.g., issues with saving the file)
            print(str(e))
            return JsonResponse({'status': 'error', 'errors': {'exception': str(e)}})

    # Fallback for any other non-AJAX or non-POST requests
    return render(request ,'dashboard/user-edit.html', context=context)


@login_required
@user_passes_test(tests.is_contributor_or_staff)
def user_view(request, id=None):
    if id is None:  # No ID is passed, show the logged-in user's profile
        user = request.user
    else:
        # Check if the user is staff or the ID matches the logged-in user
        if request.user.is_staff or request.user.pk == id:
            user = get_user_model().objects.get(pk=id)
        else:
            # Optionally, you can handle this with a redirect or permission error
            raise PermissionDenied

    context = {
        'user': user
    }
    return render(request, 'dashboard/user-view.html', context=context)
