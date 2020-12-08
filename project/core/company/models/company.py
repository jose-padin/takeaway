from django.db import models
from django.utils.translation import gettext_lazy as _
# from address.models import AddressField

from core.user.models import AdminUser


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=120,
        verbose_name=_('name'),
        null=False,
        blank=False
    )
    # address = AddressField(on_delete=models.CASCADE)
    address = models.CharField(
        verbose_name=_('address'),
        max_length=255,
        default=''
    )
    postal_code = models.IntegerField(
        verbose_name=_('postal code'),
        default=36600
    )
    description = models.CharField(
        verbose_name=_('description'),
        max_length=255
    )
    image = models.ImageField(
        verbose_name=_('image'),
        null=True,
        blank=True
    )
    logo = models.ImageField(
        verbose_name=_('logo'),
        null=True,
        blank=True
    )
    admin = models.ForeignKey(
        AdminUser,
        verbose_name=_('admin'),
        null=True,
        on_delete=models.DO_NOTHING
    )
    class Meta:
        db_table = _('company')
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name
