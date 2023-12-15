from django.contrib import admin
from . import models


@admin.action(description="Select user for make admin")
def make_be_admin(modeladmin, request, queryset):
    queryset.update(is_superuser=True)


@admin.action(description="Select user for make user")
def make_be_user(modeladmin, request, queryset):
    queryset.update(is_superuser=False)


@admin.action(description="Activate user")
def activate_user(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Deactivate user")
def deactivate_user(modeladmin, request, queryset):
    queryset.update(is_active=False)


class CustomUserModelAdmin(admin.ModelAdmin):
    list_filter = [
         "is_staff",
         "is_active",
         "is_superuser",
         "date_joined",
    ]
    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
        "phone_number",
    )

    list_display = ["username", "is_active", "is_superuser", "is_staff", "date_joined"]

    actions = [make_be_admin, make_be_user, deactivate_user, activate_user]


admin.site.register(models.CustomUser, CustomUserModelAdmin)


