# Generated by Django 5.1.1 on 2024-09-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(),
        ),
    ]
