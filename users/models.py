from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import uuid
from phonenumber_field.modelfields import PhoneNumberField

from .managers import iLKMSUserManager 


class iLKMSUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_("email Address"), unique=True)
    full_name = models.CharField("Full Name", max_length=100,  null=True, blank=True)
    phone_number = PhoneNumberField("Phone Number", null=True, blank=True, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = iLKMSUserManager()

    class Meta:
        verbose_name_plural = "iLKMS_User"
       # ordering = ["-created_date"]


    def __str__(self):
        return str(self.id)
    
