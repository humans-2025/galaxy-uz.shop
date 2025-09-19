# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, verbose_name="Telefon raqami")
    invite_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Taklif kodi")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Balans")

    USERNAME_FIELD = "phone"   # Telefon raqam bilan login
    REQUIRED_FIELDS = ["username", "email"]

    def __str__(self):
        return f"{self.phone} | {self.username}"