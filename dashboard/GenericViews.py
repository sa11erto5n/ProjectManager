# dashboard/views.py

from django.views.generic import ListView
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import View

class BaseListView(ListView):
    context_object_name = 'items'
    template_name = None  # Will be set in the subclass
    model = None  # Will be set in the subclass
    create_url = ''
    delete_url = ''
    fields = []
    title = ''
    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.fields
        context['names'] = self.names
        context['title'] = self.title
        context['create_url'] = self.create_url
        context['delete_url'] = self.delete_url
        return context

class BaseDeleteView(LoginRequiredMixin, View):
    model = None  # Change this to your model if needed

    def post(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=item_id)
        item.delete()
        return JsonResponse({'status': 'success', 'message': 'تم حذف العنصر بنجاح.'})