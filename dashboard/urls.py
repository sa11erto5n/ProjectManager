from django.urls import path, include
from . import views
from . import products_views
from . import reports_views as rp
from .contributions_views import *
from .earning_views import *
from .requests_view import RequestCreateView
from . import join_requests_views as jrv

app_name = 'dash'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('users/',views.users_view,name='users'),
    path('users/create',views.create_user,name='create_user'),
    path('users/view/<int:id>',views.user_view,name='view_user'),
    path('user/edit/<int:id>',views.user_edit,name='user_edit'),
    # Prodcuts
    path('products/',products_views.ProductsList.as_view(),name='products_list'),
    path('products/create',products_views.ProductCreate,name='create_product'),
    path('products/delete/<int:pk>',products_views.ProductDelete.as_view(),name='delete_product'),
    # Contributions 
    path('contributions/create/', ContributionCreateView.as_view(), name='create_contribution'),
    path('contributions/', ContributionListView.as_view(), name='contribution_list'),
    path('contributions/delete/<int:pk>/', ContributionDeleteView.as_view(), name='delete_contribution'),
    # Reports
    path('report/create/', rp.ReportCreateView.as_view(), name='create_report'),
    path('report/', rp.ReportListView.as_view(), name='report_list'),
    path('report/delete/<int:pk>/', rp.ReportDeleteView.as_view(), name='delete_report'),
    # Earning
    path('earnings/', EarningsList.as_view(), name='earnings_list'),
    path('earnings/create/', EarningCreateView.as_view(), name='create_earning'),
    path('earnings/delete/<int:pk>/', EarningDelete.as_view(), name='delete_earning'),
    # Request
    # path('request/create/', RequestCreateView, name='request_create'),
    path('request/create/<str:request_type>/<int:earning_id>/', RequestCreateView, name='request_create'),
    # Join 
    path('join_request', jrv.create_join_request, name='join_request_create'),
    path('join_request/list', jrv.list, name='join_request_list'),
    
    
    
]