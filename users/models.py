# transactions/models.py
from django.db import models
from users.models import CustomUser

class Deposit(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="deposits")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deposit {self.amount} by {self.user.phone}"

class Withdraw(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="withdraws")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Withdraw {self.amount} by {self.user.phone}"
