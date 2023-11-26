from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django.utils import timezone


class CustomUser(AbstractUser):
    IRANIAN_PHONE_NUMBER_PATTERN = '9(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}'
    IRANIAN_PHONE_NUMBER_VALIDATOR = RegexValidator(
        regex=IRANIAN_PHONE_NUMBER_PATTERN,
        message=_('phone number must be Iranian'),
    )
    phone_number = models.BigIntegerField(verbose_name=_('phone number'), unique=True,
                                          validators=[IRANIAN_PHONE_NUMBER_VALIDATOR])
    email = models.EmailField(null=False, unique=True)
    
    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return self.username
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        if not email:
            raise ValueError("E-mail must be required")
        
        if not password:
            raise ValueError("Password must be required")
        
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone, password):
        if not email:
            raise ValueError("E-mail must be required")
        
        if not password:
            raise ValueError("Password must be required")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


