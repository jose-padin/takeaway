from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from core.order.models import Order


class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    delivery_date = models.DateTimeField(
        verbose_name=_('Delivery date'),
        default=None
    )
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = _('delivery')
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')

    def __str__(self):
        return f'{self.user.name} - {self.delivery_date}'