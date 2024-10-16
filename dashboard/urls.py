from django.urls import path, include
from . import views
from . import products_views
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
    

    
]