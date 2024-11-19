# dashboard/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView
from django.http import JsonResponse
from . import tests
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .GenericViews import *
from django.shortcuts import get_object_or_404
from .models import Contribution
from .forms import ContributionForm

class ContributionCreateView(UserPassesTestMixin,GenericCreateView,LoginRequiredMixin):
    model = Contribution
    form_class = ContributionForm
    create_url = 'dash:create_contribution'  # Ensure this matches your URL names
    success_url = 'dash:contribution_list'
    title = _('Contributions')
    template_name = 'dashboard/create.html'  # Use the global template
    def test_func(self) :
        print(True)
        user = self.request.user
        print(tests.is_staff(user))
        return tests.is_staff(user)



class ContributionListView(UserPassesTestMixin,BaseListView, LoginRequiredMixin):
    model = Contribution
    template_name = 'dashboard/list.html'  # Specify your template for listing contributions
    create_url = 'dash:create_contribution'  # Ensure this matches your URL names
    delete_url = 'dash:delete_contribution'  # Ensure this matches your URL names
    fields = [
        (_('User'), 'user'),
        (_('Contribution Price'), 'product_price'),
    ]  
    title = _('Contributions')

    def get_queryset(self):
        # If the user is staff or superuser, return all contributions
        if self.request.user.is_staff or self.request.user.is_superuser:
            return super().get_queryset()  # Call the superclass method to get all contributions
        # Otherwise, return only the contributions for the logged-in user
        q = Contribution.objects.filter(user__id=2)
        print(f'{ q } : {self.request.user.id}')
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['fields'] = self.fields
        context['create_url'] = self.create_url
        context['delete_url'] = self.delete_url
        return context

    def test_func(self):
        # This method can be used if you want to perform additional permission checks
        user = self.request.user
        return tests.is_contributor_or_staff(user)  # This can be updated to reflect your 

class ContributionDeleteView(UserPassesTestMixin,BaseDeleteView,LoginRequiredMixin):
    model = Contribution

    def post(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=item_id)
        item.delete()
        return JsonResponse({'status': 'success', 'message': _('Contribution deleted successfully.')})
    def test_func(self) :
        user = self.request.user
        return tests.is_staff(user) 
