from django.urls import re_path

from .views import add


urlpatterns = [

    # url(r'^view$',
    #     views.view_cart,
    #     name='client_view-cart'),

    re_path(r'^add/(?P<product_id>\d+)$', add, name="add"),
    
    # url(r'^remove/product\=(?P<product_id>\d+)$',
    #     views.remove_product,
    #     name='client_view-remove_product'),

    # url(r'^remove/product\=(?P<product_id>\d+)/quantity\=(?P<quantity>\d+)$',
    #     views.remove_product,
    #     name='client_view-remove_product'),

    # url(r'^checkout$',
    #     views.checkout,
    #     name='client_view-cart_checkout'),
]
