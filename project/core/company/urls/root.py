from django.urls import path, re_path, include

from ..views.company import company_list_view, company_detail_view

urlpatterns = [
    re_path(r'^$', company_list_view, name='list'),
    re_path(r'^company/(?P<id>\d+)$', company_detail_view, name='detail'),
    # path('company/<int:id>/', company_list_view)
]