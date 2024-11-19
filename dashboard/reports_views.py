from .views import * 
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
from .models import Report
from .forms import ReportForm

class ReportCreateView(UserPassesTestMixin,GenericCreateView,LoginRequiredMixin):
    model = Report
    form_class = ReportForm
    create_url = 'dash:create_report'  # Ensure this matches your URL names
    success_url = 'dash:report_list'
    title = _('Report')
    template_name = 'dashboard/report_create.html'  # Use the global template
    def test_func(self) :
        user = self.request.user
        return tests.is_seller_or_staff(user)


class ReportListView(UserPassesTestMixin,BaseListView,LoginRequiredMixin):
    model = Report
    template_name = 'dashboard/list.html'  # Specify your template for listing contributions
    delete_url = 'dash:delete_report'  # Ensure this matches your URL names
    fields = [
        (_('User'),'user'),
        (_('Product'),'product'),
        (_('Quantity'),'quantity'),
        (_('Price'),'price'),
        (_('Returned'),'is_returned'),
        (_('Canceled'),'is_canceled'),
        (_('Creation Data'),'date_added'),
        
        ]  
    title = _('Report')
    def get_queryset(self):
        user = self.request.user
        # Adjust this logic based on your requirements
        if tests.is_staff(user):
            # If the user is a staff member, return all reports
            return self.model.objects.all()
        else:
            # If the user is not staff, return only their reports
            return self.model.objects.filter(user=user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff or self.request.user.account_type == 'seller':
            context['create_url'] = 'dash:create_report'
        return context
    def test_func(self) :
        user = self.request.user
        return tests.is_seller_or_staff(user)


class ReportDeleteView(UserPassesTestMixin,BaseDeleteView,LoginRequiredMixin):
    model = Report

    def post(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=item_id)
        item.delete()
        return JsonResponse({'status': 'success', 'message': _('Report deleted successfully.')})
    def test_func(self) :
        user = self.request.user
        return tests.is_staff(user) 
