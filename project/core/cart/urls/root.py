from django.urls import re_path
from .views import CartView

urlpatterns = [
    re_path('^', CartView.as_view)
]