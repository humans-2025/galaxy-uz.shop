from django.db import models
from django.conf import settings

class Referral(models.Model):
    inviter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="referrals"
    )
    invited = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="invited_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inviter.phone} → {self.invited.phone}"