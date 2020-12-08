from django.db import models

from .baseuser import BaseUser


class AdminUser(BaseUser):

    class Meta:
        proxy = True
