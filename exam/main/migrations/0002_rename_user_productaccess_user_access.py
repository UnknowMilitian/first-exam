# Generated by Django 5.1.1 on 2024-09-23 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productaccess',
            old_name='user',
            new_name='user_access',
        ),
    ]
