from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)
    CHOISE = (
        (1, 'admin'),
        (2, 'user')
    )
    roles = models.PositiveSmallIntegerField(default=1,choices=CHOISE) 