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
    phone_number = models.BigIntegerField(_('Phone Number'), unique=True,
                                          validators=[IRANIAN_PHONE_NUMBER_VALIDATOR])
    email = models.EmailField(_("E-mail"), null=False, unique=True)
    
    class Meta:
        ordering = ['date_joined']
        
        

    def __str__(self) -> str:
        return self.username
    
    def get_full_name(self) -> str:
        return super().get_full_name()
    
    def is_admin(self) -> bool:
        return self.is_admin
    
    def create_user(self, email:str, phone:int, password:str):
        user = self.objects.create(
            phone_number=phone, 
            email=email, 
            password=password
            )
        return user
    
    def create_superuser(self, email:str, phone:int, password:str):
        user = self.objects.create(
            phone_number=phone, 
            email=email, 
            password=password, 
            is_admin=True
            )
        return user

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, phone, password=None):
#         if not email:
#             raise ValueError("E-mail must be required")
        
#         if not password:
#             raise ValueError("Password must be required")
        
#         user = self.model(
#             email=self.normalize_email(email),
#             phone=phone,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, phone, password):
#         if not email:
#             raise ValueError("E-mail must be required")
        
#         if not password:
#             raise ValueError("Password must be required")

#         user = self.model(
#             email=email,
#             phone=phone,
#             password=password,
#         )

#         user.is_admin = True
#         user.save(using=self._db)
#         return user
    


    # @property
    # def is_admin(self):
    #     return self.admin


