from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction

@login_required
def deposit_request(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        Transaction.objects.create(user=request.user, amount=amount, type="deposit")
        return redirect("transactions:history")
    return render(request, "transactions/deposit_form.html")

@login_required
def withdraw_request(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        Transaction.objects.create(user=request.user, amount=amount, type="withdraw")
        return redirect("transactions:history")
    return render(request, "transactions/withdraw_form.html")

@login_required
def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "transactions/transaction_list.html", {"transactions": transactions})