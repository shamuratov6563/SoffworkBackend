from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator

class UserCustomManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    _validate_email = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Enter a valid email address'
    )
    _validate_phone_number = RegexValidator(
        regex=r"^9\d{12}$",
        message='Enter a valid phone number'
    )
    AUTH_ROLE = (
        ('buyer', 'buyer'),
        ('seller','seller'),
    )
    AUTH_TYPE = (
        ('email', 'email'),
        ('phone_number', 'phone_number'),
    )
    first_name = None
    last_name = None
    bio = models.TextField(null=True, blank=True)
    auth_role = models.CharField(max_length=255, choices=AUTH_ROLE)
    auth_type = models.CharField(max_length=20, choices=AUTH_TYPE)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='project/',null=True)
    email = models.EmailField(blank=True, validators=[_validate_email])
    wallet = models.PositiveIntegerField(null=True, default=0)
    confirmation_code = models.CharField(max_length=6, null=True, blank=True) 
    email_confirmed = models.BooleanField(default=False)

































