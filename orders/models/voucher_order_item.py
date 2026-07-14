from django.core.validators import MinValueValidator, MaxValueValidator
from .common import generate_random_code
from decimal import Decimal

from django.db import models


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.SET_NULL, related_name="orders_items", null=True, blank=False)

    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(20)], default=1)
    product_name = models.CharField(max_length=100)
    product_final_price = models.DecimalField(validators=[MinValueValidator(10)], max_digits=10, decimal_places=2)


class Voucher(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=12, default=generate_random_code, unique=True, editable=False)

    discount_price = models.DecimalField(validators=[MinValueValidator(10)], max_digits=10, decimal_places=2, default=Decimal("10.00"))

    is_active = models.BooleanField(default=True)