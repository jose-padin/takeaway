from django.urls import re_path, include

from ..views.product import (
    # ProductListView,
    add,
    edit,
    list_by_category,
    delete
)


urlpatterns = [
    # re_path(r'^$', ProductListView.as_view(), name='list'),
    re_path(r'^(?P<category_id>\d+)/$', list_by_category, name='list_by_category'),
    re_path(r'^(?P<category_id>\d+)/add/$', add, name='add'),
    re_path(r'^update/(?P<product_id>\d+)/$', edit, name='update'),
    re_path(r'^delete/(?P<product_id>\d+)/$', delete, name='delete'),
]