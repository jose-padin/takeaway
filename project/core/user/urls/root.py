from django.urls import re_path

from ..views.user import add_admin

urlpatterns = [
    re_path(r'^add', add_admin, name='add'),
]