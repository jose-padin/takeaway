from django.urls import re_path

from ..views import (
    add,
    form_sent,
    register
)


urlpatterns = [
    re_path(r'^$', register, name='register'),
    re_path(r'^add$', add, name='add'),
    re_path(r'^form_sent$', form_sent, name='form_sent'),
]

