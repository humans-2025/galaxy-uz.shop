from django.contrib import admin
from .models import Transaction, Deposit, Withdraw

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "amount", "status", "created_at")
    list_filter = ("type", "status", "created_at")
    search_fields = ("user__username", "user__phone")

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "user__phone")

@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "user__phone")
