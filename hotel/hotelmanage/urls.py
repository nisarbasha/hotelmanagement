from django.urls import path
from .views import *

urlpatterns = [

    path('logout_page/', logout_page, name='Logout'),
    path('login_page/', login_page),
    path('sign_up_page/', sign_up, name='sign_up'),
    path('cust_dashboard/', cust_dashboard),
    path('cust_registration_html/', cust_registration_html),
    path('customer_login/', customer_login,name="previous"),
    path('invalid/', invalid),
    path('cust_room_booking/', cust_room_booking),
    path('cust_home_page/',cust_home_page,name="back"),
    path('sample/',sample),
    path('generate_bill_code/',generate_bill_code),
    path('mysign_up/',mysign_up),

    ]