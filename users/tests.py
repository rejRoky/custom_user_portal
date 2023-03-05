from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    # def test_create_user(self):
    #     User = get_user_model()
    #     user = User.objects.create_user(phone_number = "+880888998822", full_name = "normal user", email="normal@user.com", password="foo")
    #     self.assertEqual(user.email, "normal@user.com")
    #     self.assertTrue(user.is_active)
    #     self.assertFalse(user.is_staff)
    #     self.assertFalse(user.is_superuser)
    #     try:
    #         # username is None for the AbstractUser option
    #         # username does not exist for the AbstractBaseUser option
    #         self.assertIsNone(user.username)
    #     except AttributeError:
    #         pass
    #     with self.assertRaises(TypeError):
    #         User.objects.create_user()
    #     with self.assertRaises(TypeError):
    #         User.objects.create_user(phone_number = "0123", full_name = "", email="a@test.com", password="a@test")
    #     with self.assertRaises(ValueError):
    #         User.objects.create_user(phone_number = "4567", full_name = "", email="b@test.com", password="b@test")

    def create_superuser(self):
        User = get_user_model()
        
        admin_user = User.objects.create_superuser(phone_number = "+880", full_name = "Super user", email="roky@dream71.com")
        ps="roky@dream71"
        admin_user.set_password(ps)
        admin_user.save()
        self.assertEqual(admin_user.email, "roky@dream71.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
               phone_number = "+8801888998822", full_name = "Super user", email="roky@dream71.com", password="Roky@dream71", is_superuser=False)