from .common import Payment, PaymentStatus, Status, generate_random_code
from django.db import models


class Order(models.Model):
    buyer = models.ForeignKey("users.User", on_delete=models.SET_NULL, related_name="orders", null=True, blank=False)
    order_number = models.CharField(max_length=12, unique=True, default=generate_random_code, editable=False)
    
    total_payment =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    voucher_used = models.ForeignKey("Voucher", on_delete=models.SET_NULL, related_name="orders", null=True, blank=False)
    payment_method = models.CharField(max_length=2, choices=Payment.choices, default=Payment.CASH)
    payment_status = models.CharField(max_length=2, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

    shipping_address = models.ForeignKey("users.Address", on_delete=models.SET_NULL, null=True, blank=False)
    shipping_name = models.CharField(max_length=100)
    shipping_city = models.CharField(max_length=50)
    shipping_street = models.CharField(max_length=200)
    shipping_phone = models.CharField(max_length=20)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)