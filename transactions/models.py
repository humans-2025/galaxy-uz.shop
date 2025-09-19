from django.db import models
from django.conf import settings

class Transaction(models.Model):
    TYPE_CHOICES = (
        ("deposit", "Depozit"),
        ("withdraw", "Pul yechish"),
    )
    STATUS_CHOICES = (
        ("pending", "Kutilmoqda"),
        ("approved", "Tasdiqlandi"),
        ("rejected", "Rad etildi"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount} USDT"