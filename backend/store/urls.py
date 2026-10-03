
from django.urls import path

from .views import (
    home,
    admin_dashboard,
    admin_products,
    add_product,
    login_view,
    register_view,
    checkout,
)


urlpatterns = [

    path('', home, name='home'),

    path(
        'admin-dashboard/',
        admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'admin-products/',
        admin_products,
        name='admin_products'
    ),

    path(
        'admin-products/add/',
        add_product,
        name='add_product'
    ),

    path('login/', login_view, name='login'),

    path('register/', register_view, name='register'),

    path('checkout/', checkout, name='checkout'),

]

