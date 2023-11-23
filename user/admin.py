from django.contrib import admin
from . import models

class CustomUserModelAdmin(admin.ModelAdmin):
    list_filter = [
         "is_staff",
         "is_active",
    ]
    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )

admin.site.register(models.CustomUser, CustomUserModelAdmin)


