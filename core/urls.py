from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('user_auth.urls', namespace='user_auth')),
    path('', include('frontend.urls', namespace='frontend')),
    path('dashboard/', include('dashboard.urls', namespace='dash')),
    path('translate/', include('rosetta.urls')),

    
]

# Serving static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
