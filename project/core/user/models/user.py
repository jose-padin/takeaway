from django.db import models

from .baseuser import BaseUser

class User(BaseUser):

    class Meta:
        proxy = True