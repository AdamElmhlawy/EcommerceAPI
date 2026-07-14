from rest_framework import serializers
from ..models import Product, ProductImage, Brand, Category

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image',)

class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)

    def get_final_price(self, obj):
        if obj.discount_price:
            return obj.price - obj.discount_price
        return obj.price

    class Meta:
        model = Product
        fields = (
            "name", "slug", "brand",
            "categories", "description", "price",
            "discount_price", "final_price", "thumbnail",
            "images", "stock", "rating",
            "is_active", "created_at", "updated_at",
        )
        read_only_fields = ("slug", "final_price", "rating", "created_at", "updated_at")