from django.db import models
from django.conf import settings
from django.utils.timezone import now, timedelta

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_profit = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(default=365)
    is_active = models.BooleanField(default=True)  # 🔑 VIP faolligini boshqarish

    def __str__(self):
        return f"{self.name} - ${self.price} ({'Faol' if self.is_active else 'Tez orada'})"


class UserProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = now() + timedelta(days=self.product.duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.phone} → {self.product.name}"