from django.urls import re_path, include

from ..views.company import company_list_view 

urlpatterns = [
    re_path(r'^$', company_list_view, name='list'),
    # re_path(r'^(?P<id>\d+)', include())
]