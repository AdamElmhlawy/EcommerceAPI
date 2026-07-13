from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']
