# Generated by Django 5.1.1 on 2024-09-23 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_lesson_duration_alter_lesson_url_to_video_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='productaccess',
            name='user_access',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_accesses', to=settings.AUTH_USER_MODEL),
        ),
    ]
