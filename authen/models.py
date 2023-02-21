from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, phone, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractUser):
    phone = PhoneNumberField(unique=True)
    USERNAME_FIELD = 'phone'
    objects = MyUserManager()

