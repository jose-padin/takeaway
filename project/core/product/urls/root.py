from django.urls import re_path, include

from ..views.product import ProductListView

urlpatterns = [
    re_path('^', ProductListView.as_view(), name='list'),
]