from django.contrib import admin
from .models import Deposit, Withdraw

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__phone",)

    actions = ["approve_deposits", "reject_deposits", "mark_as_paid"]

    def approve_deposits(self, request, queryset):
        queryset.update(status="approved")
    approve_deposits.short_description = "Tanlangan depozitlarni tasdiqlash"

    def reject_deposits(self, request, queryset):
        queryset.update(status="rejected")
    reject_deposits.short_description = "Tanlangan depozitlarni rad etish"

    def mark_as_paid(self, request, queryset):
        for deposit in queryset:
            if deposit.status == "approved":
                deposit.status = "paid"
                deposit.user.balance += deposit.amount  # ✅ balansga qo‘shamiz
                deposit.user.save()
                deposit.save()
    mark_as_paid.short_description = "Tasdiqlangan depozitlarni hisobga o‘tkazish"


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "trc20_address", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__phone", "trc20_address")

    actions = ["approve_withdraws", "reject_withdraws", "mark_as_paid"]

    def approve_withdraws(self, request, queryset):
        queryset.update(status="approved")
    approve_withdraws.short_description = "Tanlangan yechib olishlarni tasdiqlash"

    def reject_withdraws(self, request, queryset):
        for withdraw in queryset:
            if withdraw.status == "pending":
                withdraw.status = "rejected"
                withdraw.user.balance += withdraw.amount  # ✅ balans qaytariladi
                withdraw.user.save()
                withdraw.save()
    reject_withdraws.short_description = "Tanlangan yechib olishlarni rad etish"

    def mark_as_paid(self, request, queryset):
        queryset.update(status="paid")
    mark_as_paid.short_description = "Tanlangan yechib olishlarni to‘langan deb belgilash"