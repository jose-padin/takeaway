from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# from core.client.models import Client
from core.product.models import Product

ORDER_TYPE = [
    ('TK', 'To takeaway'),
    ('CO', 'To collect'),
]


class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = _('order_product')
        verbose_name = _('Order product')
        verbose_name_plural = _('Order products')

    # def __str__(self):
    #     return f'{self.order.name}: {self.product.name}'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(
        verbose_name=_('Date'),
        default=timezone.now(),
    )
    # type: to takeaway or to collect
    order_type = models.CharField(
        verbose_name=_('Order type'),
        max_length=2,
        null=False,
        choices=ORDER_TYPE,
        default='TK'
    )
    products = models.ManyToManyField(Product, through=OrderProduct)

