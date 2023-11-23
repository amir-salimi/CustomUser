from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    IRANIAN_PHONE_NUMBER_PATTERN = '9(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}'
    IRANIAN_PHONE_NUMBER_VALIDATOR = RegexValidator(
        regex=IRANIAN_PHONE_NUMBER_PATTERN,
        message=_('phone number must be Iranian'),
    )
    phone_number = models.BigIntegerField(verbose_name=_('phone number'), unique=True,
                                          validators=[IRANIAN_PHONE_NUMBER_VALIDATOR])
    # phone_number = models.BigIntegerField(default=9187600330)
    email = models.EmailField(null=False)
    
    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return self.username