from django.contrib.auth.base_user import BaseUserManager
from .Person import Person

"""
Custom User manager associated to the CustomUser model

Tutorial I used:
https://dev.to/chokshiroshan/how-to-use-email-as-username-for-django-authentication-8if
"""
class CustomUserManager(BaseUserManager):

    def create_user(self, email, person, password=None, **extra_fields):
        
        email = self.normalize_email(email)
        user = self.model(email=email,person = Person.objects.get(id=person), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, person, password, **extra_fields):
        
        user = self.create_user(email, person, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
    