from django.contrib import admin

from .models.product import Product, Category, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    pass



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Category)