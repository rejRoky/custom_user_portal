from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import iLKMSUser


class iLKMSUserCreationForm(UserCreationForm):

    class Meta:
        model = iLKMSUser
        fields = ("full_name","email","phone_number", "is_superuser", "is_staff", "is_active", "date_joined",)


class iLKMSUserChangeForm(UserChangeForm):

    class Meta:
        model = iLKMSUser
        fields = ("full_name","email","phone_number", "is_superuser", "is_staff", "is_active", "date_joined",)



from phonenumber_field.formfields  import PhoneNumberField

class PhoneForm(forms.Form):
    phone_number = PhoneNumberField(region="CA")