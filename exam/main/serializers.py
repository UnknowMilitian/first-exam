from rest_framework import serializers
from .models import Product, ProductAccess, Lesson, LessonProgress


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "user", "title", "created_at"]


class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = ["id", "user-access", "product", "can_edit", "can_view", "granted_at"]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "products", "title", "url_to_video", "duration"]


class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = [
            "id",
            "lesson",
            "user",
            "watched_seconds",
            "is_watched",
            "last_watched_at",
        ]
        read_only_fields = ["is_watched", "last_watched_at"]
