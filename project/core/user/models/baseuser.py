import sys
from pprint import PrettyPrinter

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


class BaseUser(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        USER = 'User', 'User'

    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(
        verbose_name=_('phone number'),
        max_length=9
    )
    email = models.EmailField(
        verbose_name=_('email'),
        unique=True
    )
    type = models.CharField(
        verbose_name=_('type'),
        max_length=50,
        choices=Types.choices,
        default=Types.USER
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = _('baseuser')
        verbose_name = _('Base user')
        verbose_name_plural = _('Base users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
