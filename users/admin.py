from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import iLKMSUserCreationForm, iLKMSUserChangeForm
from .models import iLKMSUser


class iLKMSUserAdmin(UserAdmin):
    add_form = iLKMSUserCreationForm
    form = iLKMSUserChangeForm
    model = iLKMSUser
    list_display = ("id","full_name","email","phone_number", "is_superuser", "is_staff", "is_active", "date_joined",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("full_name","email","phone_number")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "full_name","email","phone_number", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("phone_number", "email",)
    ordering = ("date_joined",)


admin.site.register(iLKMSUser, iLKMSUserAdmin)