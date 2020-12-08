from django.urls import re_path

from ..views import (
    add,
    add_category,
    list_categories,
    form_sent,
    register,
    edit_category,
    delete_category
)


urlpatterns = [
    re_path(r'^$', register, name='register'),
    re_path(r'^add$', add, name='add'),
    re_path(r'^add_category$', add_category, name='add_category'),
    re_path(r'^list_categories$', list_categories, name='list_categories'),
    re_path(r'^edit_category/(?P<category_id>\d+)/$', edit_category, name='edit_category'),
    re_path(r'^delete_category/(?P<category_id>\d+)/$', delete_category, name='delete_category'),
    re_path(r'^form_sent$', form_sent, name='form_sent'),
]

