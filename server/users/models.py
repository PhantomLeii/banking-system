from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManger


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_TYPES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, null=True, blank=True, choices=GENDER_TYPES
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManger()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def has_module_perms(self, app_label: str) -> bool:
        return True

    def has_perm(self, perm: str, obj=None) -> bool:
        return True

    def __str__(self):
        return self.email
