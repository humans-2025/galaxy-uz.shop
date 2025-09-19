from django.shortcuts import render
from .models import Product, UserProduct

def product_list(request):
    # Faqat faol mahsulotlarni sotib olish mumkin
    active_products = Product.objects.filter(is_active=True)
    # Passiv mahsulotlar alohida ko‘rsatiladi
    upcoming_products = Product.objects.filter(is_active=False)
    return render(request, "products/product_list.html", {
        "active_products": active_products,
        "upcoming_products": upcoming_products
    })