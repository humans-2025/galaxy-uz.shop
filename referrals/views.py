from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Referral

@login_required
def my_referrals(request):
    referrals = Referral.objects.filter(inviter=request.user)
    return render(request, "referrals/my_referrals.html", {"referrals": referrals})