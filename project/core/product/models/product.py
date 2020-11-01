from django.db import models
from django.utils.translation import gettext_lazy as _

# from core.category.models import Category
from core.company.models import Company


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
        blank=False,
        null=False
    )
    description = models.CharField(
        max_length=255,
        verbose_name=_('Description'),
    )
    allergens = models.CharField(
        max_length=100,
        verbose_name=_('Allergens'),
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name = _('Price'),
        max_digits=8,
        decimal_places=2
    )
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    # category = models.ManyToManyField(Category, through='ProductCategory')
    # category = models.ManyToManyField(
    #     'category.Category',
    #     # on_delete=models.DO_NOTHING,
    #     # null=True,
    #     # blank=True
    #     # through='ProductCategory'
    # )

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table = 'product_category'
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    def __str__(self):
        return f'{self.category.name}: {self.product.name}'

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=150,
        verbose_name = _('Name'),
        null=False,
        blank=False
    )
    products = models.ManyToManyField(Product, through=ProductCategory)
    # product = models.ManyToManyField('Product')

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



