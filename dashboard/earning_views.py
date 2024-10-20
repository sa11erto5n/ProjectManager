from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Earning
from . import GenericViews as gv
from . import forms
from . import tests
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from . import tests


class EarningsList(UserPassesTestMixin,gv.BaseListView, LoginRequiredMixin):
    model = Earning
    template_name = 'dashboard/list.html'
    create_url = 'dash:create_earning'
    delete_url = 'dash:delete_earning'
    fields = [
        (_('User Earnings'), 'user'),
        (_('Earned Price'), 'earning'),
        (_('Product'), 'product'),
        (_('Date Added'), 'date_added'),
    ]
    names = [_('Earned Price')]
    title = _('Earnings List')
    def get_queryset(self):
        user = self.request.user
        # Adjust this logic based on your requirements
        if tests.is_staff(user):
            # If the user is a staff member, return all reports
            return self.model.objects.all()
        else:
            # If the user is not staff, return only their reports
            return self.model.objects.filter(user=user)

    def test_func(self):
        user = self.request.user
        return tests.is_contributor_or_staff(user)

class EarningCreateView(UserPassesTestMixin,gv.GenericCreateView,LoginRequiredMixin):
    model = Earning
    form_class = forms.EarningForm
    create_url = 'dash:create_earning'  # Ensure this matches your URL names
    success_url = 'dash:earnings_list'
    title = _('Report')
    template_name = 'dashboard/create.html'  # Use the global template
    def test_func(self) :
        user = self.request.user
        return tests.is_staff(user)

class EarningDelete(UserPassesTestMixin, gv.BaseDeleteView, LoginRequiredMixin):
    model = Earning
    success_url = 'dash:earnings_list'
    def test_func(self) -> bool | None:
        user = self.request.user
        return tests.is_staff(user)
