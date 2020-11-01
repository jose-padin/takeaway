from django.db import models
from django.utils.translation import gettext_lazy as _
# from address.models import AddressField


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=120,
        verbose_name=_('Company'),
        null=False,
        blank=False
    )
    # address = AddressField(on_delete=models.CASCADE)

    class Meta:
        db_table = _('company')
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name
