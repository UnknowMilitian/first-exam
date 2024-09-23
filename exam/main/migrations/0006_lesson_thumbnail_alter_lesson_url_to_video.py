# Generated by Django 5.1.1 on 2024-09-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_productaccess_user_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails', verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='url_to_video',
            field=models.FileField(upload_to='lesson', verbose_name='Lesson file video'),
        ),
    ]
