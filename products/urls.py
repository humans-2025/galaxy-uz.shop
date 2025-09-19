from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("buy/<int:product_id>/", views.buy_product, name="buy_product"),
    path("my/", views.my_products, name="my_products"),
]