from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

from django.db import models

from .common import SlugModel


class Product(SlugModel):
    brand = models.ForeignKey("Brand", on_delete=models.PROTECT, related_name="products")
    categories = models.ManyToManyField("Category", related_name="products")

    description = models.TextField()

    price = models.DecimalField(validators=[MinValueValidator(10)], max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(validators=[MinValueValidator(0)], max_digits=10, decimal_places=2, default=Decimal(0.00))

    stock = models.PositiveIntegerField(validators=[MaxValueValidator(1000)], default=0)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)

    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()

        if self.discount_price > self.price:
            raise ValidationError({"discount_price": "Discount price cannot be greater than the original price."})
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product.name} image"