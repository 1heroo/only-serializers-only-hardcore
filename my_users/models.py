from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=False, blank=True)
    email = models.EmailField(
        _("email address"),
        unique=True
    )
    code = models.CharField(max_length=10, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return f'{super().first_name} {super().last_name}'
