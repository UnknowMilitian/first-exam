from rest_framework import serializers
from .models import Product, ProductAccess


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "user", "title", "created_at"]


class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = ["id", "user-access", "product", "can_edit", "can_view", "granted_at"]
