from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

@login_required
def chat_with_admin(request):
    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        return render(request, "chat/no_admin.html")

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Message.objects.create(sender=request.user, receiver=admin_user, text=text)
            return redirect("chat:chat_with_admin")

    messages = Message.objects.filter(
        sender__in=[request.user, admin_user],
        receiver__in=[request.user, admin_user]
    ).order_by("created_at")

    return render(request, "chat/chat.html", {"messages": messages, "admin": admin_user})