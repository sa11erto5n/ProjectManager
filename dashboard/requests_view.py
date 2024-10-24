from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import RequestForm
from .models import Request,Earning, NotificationsCounter
from .context_processors import global_context
from . import tests

from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _

@login_required
def RequestCreateView(request, request_type, earning_id):
    # Check if the user is a contributor
    if not tests.is_contributor(request.user):
        raise PermissionDenied(_("You do not have permission to create a request."))

    # Ensure the request_type is valid
    if request_type not in ['refund', 'reinvest']:
        raise PermissionDenied(_("Invalid request type."))

    # Fetch the Earning object
    earning = get_object_or_404(Earning, id=earning_id)

    # Create the request based on the type and save it
    new_request = Request.objects.create(
        user=request.user,
        earning=earning,
        project=earning.product,  # Assuming 'project' is linked to 'Earning'
        request_type=request_type
    )

    # Increment the notifications counter
    counter, created = NotificationsCounter.objects.get_or_create(id=1)
    counter.count += 1
    counter.save()

    # Redirect to the dashboard after creation
    return redirect('dash:home')
