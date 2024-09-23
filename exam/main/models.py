from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from moviepy.editor import *


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product")
    title = models.CharField(_("Product title"), max_length=255)
    created_at = models.DateTimeField(_("Product created date"), auto_now_add=True)

    def __str__(self):
        return f"Product - {self.title}"


class ProductAccess(models.Model):
    user_access = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_accesses"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    can_edit = models.BooleanField(_("Can edit"), default=False)
    can_view = models.BooleanField(_("Can view"), default=True)
    granted_at = models.DateTimeField(_("Granted at"), auto_now_add=True)

    def __str__(self):
        return f"User '{self.user_access}' has access to product '{self.product.title}'"


class Lesson(models.Model):
    products = models.ManyToManyField(Product, related_name="lessons")
    title = models.CharField(_("Lesson title"), max_length=250)
    url_to_video = models.FileField(_("Lesson file video"), upload_to="lesson")
    thumbnail = models.ImageField(
        _("Thumbnail"), upload_to="thumbnails", blank=True, null=True
    )
    duration = models.IntegerField()  # Duration in seconds

    def __str__(self):
        return self.title


class LessonProgress(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="progress"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lesson_progress"
    )
    watched_seconds = models.IntegerField(default=0)
    is_watched = models.BooleanField(default=False)
    last_watched = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.watched_seconds >= 0.8 * self.lesson.duration:
            self.is_watched = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} progress for {self.lesson.title}"
