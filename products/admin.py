from django.contrib import admin
from .models import Product, UserProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "daily_profit", "duration_days", "is_active")
    list_editable = ("is_active",)  # 🔑 Admin paneldan tez o‘zgartirish mumkin
    search_fields = ("name",)
    list_filter = ("is_active", "duration_days")

@admin.register(UserProduct)
class UserProductAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "purchase_date", "expiry_date")
    search_fields = ("user__phone", "product__name")
    list_filter = ("purchase_date", "expiry_date")