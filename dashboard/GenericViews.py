# dashboard/views.py
from django.shortcuts import render

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
        context['title'] = self.title
        context['create_url'] = self.create_url
        context['delete_url'] = self.delete_url
        return context

class GenericCreateView(View):
    model = None
    form_class = None
    create_url = ''
    success_url = ''
    template_name = 'dashboard/create.html'  # Updated to point to the global template
    success_url = ''
    title = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {
            'form': form, 
            'title': self.title,
            'create_url' : self.create_url,
            'success_url' : self.success_url})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', f'{self.model.__name__.lower()}_id': instance.id})
        else:
            # Collect error messages
            errors = {field: list(errors) for field, errors in form.errors.items()}
            return JsonResponse({'status': 'error', 'errors': errors})


class BaseDeleteView(LoginRequiredMixin, View):
    model = None  # Change this to your model if needed

    def post(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=item_id)
        item.delete()
        return JsonResponse({'status': 'success', 'message': 'تم حذف العنصر بنجاح.'})