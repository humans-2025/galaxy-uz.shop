from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("support/", views.chat_with_admin, name="chat_with_admin"),
]