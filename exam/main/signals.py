from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lesson
from moviepy.editor import VideoFileClip
import os


@receiver(post_save, sender=Lesson)
def create_thumbnail(sender, instance, created, **kwargs):
    if created:
        video_path = instance.url_to_video.path
        thumbnail_path = os.path.join(
            "thumbnails", f"{os.path.basename(video_path).split('.')[0]}_thumbnail.jpg"
        )

        with VideoFileClip(video_path) as video:
            # Generate the thumbnail
            video.save_frame(
                os.path.join("media", thumbnail_path), t=1
            )  # Save to media/thumbnails

            # Get the video duration in seconds
            duration = int(video.duration)  # Get duration in seconds

        instance.thumbnail = thumbnail_path  # Save thumbnail path to the instance
        instance.duration = duration  # Set duration
        instance.save(
            update_fields=["thumbnail", "duration"]
        )  # Update the model instance
