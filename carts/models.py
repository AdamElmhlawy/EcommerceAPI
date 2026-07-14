from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

class CartItem(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="cart_items")

    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], default=1)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "product"], name="unique_cart_product")]


class SavedItem(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="saved_items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="saved_items")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "product"], name="unique_saved_product")]
    