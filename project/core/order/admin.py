from django.contrib import admin

from .models.order import Order, OrderProduct

admin.site.register(Order)
admin.site.register(OrderProduct)
