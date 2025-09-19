from django.urls import path
from . import views

app_name = "referrals"

urlpatterns = [
    path("my/", views.my_referrals, name="my_referrals"),
]