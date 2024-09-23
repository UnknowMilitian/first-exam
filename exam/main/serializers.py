from django.db import models
from rest_framework import serializers
from .models import Product, ProductAccess, Lesson, LessonProgress, User


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


# Final Serializer for product statistic
class ProductStatisticsSerializer(serializers.ModelSerializer):
    lessons_viewed = serializers.SerializerMethodField()
    total_watch_time = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()
    acquisition_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "lessons_viewed",
            "total_watch_time",
            "student_count",
            "acquisition_percentage",
        ]

    def get_lessons_viewed(self, product):
        return LessonProgress.objects.filter(lesson__products=product).count()

    def get_total_watch_time(self, product):
        return (
            LessonProgress.objects.filter(lesson__products=product).aggregate(
                total=models.Sum("watched_seconds")
            )["total"]
            or 0
        )

    def get_student_count(self, product):
        return product.productaccess_set.filter(can_view=True).count()

    def get_acquisition_percentage(self, product):
        total_users = User.objects.count()
        access_count = product.productaccess_set.count()
        if total_users == 0:
            return 0
        return (access_count / total_users) * 100
