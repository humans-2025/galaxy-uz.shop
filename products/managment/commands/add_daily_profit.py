from django.core.management.base import BaseCommand
from django.utils import timezone
from products.models import UserProduct
from transactions.models import Deposit

class Command(BaseCommand):
    help = "Har kuni foydalanuvchilarga VIP daromad qo‘shadi"

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        active_products = UserProduct.objects.filter(expiry_date__gte=today)

        for up in active_products:
            user = up.user
            profit = up.product.daily_profit
            user.balance += profit
            user.save()

            # tarixga yozamiz
            Deposit.objects.create(
                user=user,
                amount=profit,
                status="approved"
            )

            self.stdout.write(self.style.SUCCESS(
                f"{user.phone} foydalanuvchisiga {profit} qo‘shildi"
            ))