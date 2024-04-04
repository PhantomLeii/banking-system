from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    ETHNICITY_CHOICES = (
        ('black', 'Black'),
        ('white', 'White'),
        ('other', 'Other'),
    )
    username = None
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    ethnicity = models.CharField(max_length=10, choices=ETHNICITY_CHOICES)
    street_number = models.IntegerField(blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    suburb = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name', 'surname', 'gender', 'city', 'phone_number')

    objects = UserManager()

    def __str__(self):
        return self.email
