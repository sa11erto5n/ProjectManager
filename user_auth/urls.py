from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    # auth views
    path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),  # Add the logout URL

]