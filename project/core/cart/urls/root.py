from django.urls import re_path

from ..views.views import (
    add,
    clear,
    checkout,
    list_view
)


urlpatterns = [
    re_path(r'^$', list_view, name='list_cart'),    
    re_path(r'^add/(?P<product_id>\d+)$', add, name='add'),
    re_path(r'^clear/(?P<company_id>\d+)$', clear, name='clear'),
    re_path(r'^checkout/$', checkout, name='checkout'),
]
