from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser
from django.utils.translation import gettext_lazy as _


class User(EmailAbstractUser):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("P", "Prefer Not To Say"),
        ("O", "Other"),
    )

    date_of_birth = models.DateField(_("Date of Birth"), null=True, blank=True)
    phone_number = models.CharField(
        _("Phone Number"), null=True, blank=True, max_length=15
    )
    gender = models.CharField(
        _("Gender"), null=True, blank=True, choices=GENDER_CHOICES, max_length=5
    )

    objects = EmailUserManager()

    def __str__(self):
        return self.email
