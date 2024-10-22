from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import RequestForm
from .models import Request, NotificationsCounter
from .context_processors import global_context
from . import tests

@login_required
def RequestCreateView(request):
    # Check if the user is a contributor using your test function
    if not tests.is_contributor(request.user):
        raise PermissionDenied(_("You do not have permission to create a request."))

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            # Set the logged-in user as the request creator
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            counter, created = NotificationsCounter.objects.get_or_create(id=1)
            counter.count += 1
            counter.save()  # Save the updated count
            return redirect(reverse_lazy('dash:home'))  # Redirect after success
    else:
        form = RequestForm()

    return render(request, 'dashboard/create_request.html', {
        'form': form
    })
