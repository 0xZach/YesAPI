from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Permission

from django.core.mail import send_mail
from django.utils import timezone

from .CustomUserManager import CustomUserManager
from .Person import Person


"""
Custom User model for the api authentication

tutorial I used:
https://testdriven.io/blog/django-custom-user-model/
"""
class CustomUser(AbstractBaseUser,PermissionsMixin):

    # Attributes 

    email = models.EmailField(unique=True, max_length=255, blank=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="FK_person")
    is_active = models.BooleanField(default=True)
    user_permissions = models.ManyToManyField(Permission,blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['person']

    # this allows to bypass the original user manager and instead use the one we created
    objects = CustomUserManager()



    # Methods

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Email this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

