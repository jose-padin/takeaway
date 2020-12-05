from django.urls import path, re_path, include

from ..views.company import company_list_view, company_detail_view

urlpatterns = [
    re_path(r'^$', company_list_view, name='list'),
    re_path(r'^company/(?P<company_id>\d+)$', company_detail_view, name='detail'),
    # re_path(r'^company/(?P<company_id>\d+)/cart/', include(('core.cart.urls', 'cart'))),
]