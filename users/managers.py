from django.contrib.auth.base_user import BaseUserManager


class CustomBaseUser(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **other_fields):
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **other_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **other_fields
    ):
        user = self.create_user(email, first_name, last_name, password, **other_fields)
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
