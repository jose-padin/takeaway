from django.urls import re_path

from ..views.views import (
    add,
    delete,
    clear,
    checkout,
    list_view
)


urlpatterns = [
    re_path(r'^$', list_view, name='list'),    
    re_path(r'^add/(?P<product_id>\d+)$', add, name='add'),
    re_path(r'^delete/(?P<product_id>\d+)/(?P<company_id>\d+)/$', delete, name='delete'),
    re_path(r'^clear/(?P<company_id>\d+)$', clear, name='clear'),
    re_path(r'^checkout/$', checkout, name='checkout'),
]
