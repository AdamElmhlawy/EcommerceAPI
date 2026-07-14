from rest_framework import serializers
from ..models import Brand, Category

class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.StringRelatedField(source="parent", read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'description', 'parent', 'parent_name')
        read_only_fields = ("slug",)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("name", "slug")
        read_only_fields = ("slug",)