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


class LessonWithProgressSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ["id", "products", "title", "url_to_video", "duration", "progress"]

    def get_progress(self, lesson):
        user = self.context["request"].user
        try:
            progress = LessonProgress.objects.get(lesson=lesson, user=user)
            return {
                "watched_seconds": progress.watched_seconds,
                "is_watched": progress.is_watched,
                "last_watched": progress.last_watched,
            }
        except LessonProgress.DoesNotExist:
            return {
                "watched_seconds": 0,
                "is_watched": False,
                "last_watched": None,
            }
