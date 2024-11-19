# your_app/templatetags/menu_tags.py

from django import template

from django.utils.decorators import method_decorator
from ..menus import menu_items

register = template.Library()

@register.inclusion_tag('parts/menu_template.html')
def render_menu(request):
    """Renders the menu with user staff status."""
    return {
        'menu_items': menu_items,
        'type': request.user.account_type, 
        'is_staff': request.user.is_staff, 
        
    }

@register.filter
def get_attr(obj, attr):
    """Get an attribute from an object dynamically."""
    return getattr(obj, attr, None)