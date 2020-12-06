from django.urls import re_path

from ..views.views import login_user, logout_user

urlpatterns = [
    re_path(r'^', login_user, name='login'),
    re_path(r'^logout', logout_user, name='logout'),
]