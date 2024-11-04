from .views import *
from .models import JoinRequests
from django.utils.translation import gettext as _


@csrf_exempt
def create_join_request(request):
    admin = get_user_model().objects.filter(is_superuser=True,is_staff=True).first()
    
    if request.method == 'POST':
        name = request.POST.get('r_name')
        email = request.POST.get('r_email')
        phone = request.POST.get('r_phone')
        role = request.POST.get('r_role')

        # Validate unique email and phone number
        if JoinRequests.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': _("Email already exists")})
        if JoinRequests.objects.filter(phone=phone).exists():
            return JsonResponse({'status': 'error', 'message': _("Phone number already exists")})
        try:
            # Create new join request
            JoinRequests.objects.create(
                name=name,
                email=email,
                phone=phone,
                role=role
            )
            admin.orders_count +=1 
            admin.save()
            return JsonResponse({'status': 'success', 'message': _("Request submitted. Please wait for a reply.")})
        except Exception as e:
            print(str(e))

    return JsonResponse({'status': 'error', 'message': _("Invalid request method")})

def list(request):
    context = {}
    admin = get_user_model().objects.filter(is_superuser=True,is_staff=True).first()
    
    if not request.user.is_superuser:
        return redirect('dash:home')
    admin.orders_count = 0
    admin.save()
    context['objects'] = JoinRequests.objects.all().order_by('-created_at')
    return render(request,template_name='dashboard/join_requests.html',context=context)

        