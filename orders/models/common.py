from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

from django.db import models

class Payment(models.TextChoices):
    CASH = "CA", _("Cash")
    VISA = "VS", _("Visa")
    WALLET = "WT", _("Wallet")
    FAWRY_PAY = "FP", _("Fawry_pay")

class Status(models.TextChoices):
    PENDING = 'PE', _('Pending')
    PREPARING = 'PR', _('Preparing')
    SHIPPED = 'SH', _('Shipped')
    DELIVERED = 'DE', _('Delivered')

class PaymentStatus(models.TextChoices):
    PENDING = "PE", "Pending"
    PAID = "PA", "Paid"
    FAILED = "FA", "Failed"

def generate_random_code():
    # Generates a random 12-character alphanumeric string
    return get_random_string(length=12)