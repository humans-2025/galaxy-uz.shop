from django.contrib import admin
from .models import Referral

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("inviter", "invited", "created_at")