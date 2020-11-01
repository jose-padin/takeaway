from ..views.product import ProductListView

from django.urls import re_path, include

urlpatterns = [
    re_path('^$', ProductListView.as_view(), name='list'),
]