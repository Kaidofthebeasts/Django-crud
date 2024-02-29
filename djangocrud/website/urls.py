
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    # path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('record/<int:pk>',views.customer_record,name='record'),
    path('delete_record/<int:pk>',views.delete_customer_record,name='delete_cust_record'),
    path('delete_product_record/<int:pk>',views.delete_product_record,name='delete_product_record'),
    path('add_customer/',views.add_customer,name='add_cust'),
    path('add_product/',views.add_product,name='add_prod'),
    path('update_record/<int:pk>',views.update_customer_record,name='update_cust'),
    path('update_product_record/<int:pk>',views.update_product_record,name='update_prod'),
    path('product/<int:pk>',views.product_record,name='product'),
    
    
]