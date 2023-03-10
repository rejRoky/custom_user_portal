from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class iLKMSUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone_number ,full_name, email, password, date_of_birth, national_id, address,  **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone_number:
            raise ValueError(_("The phone number must be set"))
        
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        phone_number = phone_number
        date_of_birth = date_of_birth
        national_id = national_id
        full_name = full_name
        address = address

        user = self.model(phone_number=phone_number ,email=email, full_name=full_name, date_of_birth = date_of_birth, national_id = national_id, address = address, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, full_name, email, password, date_of_birth, national_id, address,  **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user( phone_number, full_name, email, password, date_of_birth, national_id, address, **extra_fields)