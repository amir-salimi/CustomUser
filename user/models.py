from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.PositiveBigIntegerField(null=False, unique=True)
    email = models.EmailField(null=False)
    
    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return self.username