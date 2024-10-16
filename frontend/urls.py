from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('article/', views.article_details_view, name='article'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy-policy'),
    path('terms-and-conditions/', views.terms_conditions_view, name='terms-and-conditions'),
    
    
]