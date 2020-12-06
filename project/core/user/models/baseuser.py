from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseUser(models.Model):
    class Types(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        USER = 'User', 'User'

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=120,
        verbose_name=_('name'),
        null=False,
        blank=False
    )
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=120)
    phone_number = models.CharField(max_length=6)
    type = models.CharField(
        verbose_name=_('Type'),
        max_length=50,
        choices=Types.choices,
        default=Types.USER
    )

    class Meta:
        db_table = _('baseuser')
        verbose_name = _('Base user')
        verbose_name_plural = _('Base users')

    def __str__(self):
        return self.email