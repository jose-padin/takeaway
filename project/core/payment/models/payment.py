from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from core.order.models import Order


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(
        verbose_name = _('Amount'),
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        db_table = _('payment')
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return f'{self.user.name}: {self.amount}'