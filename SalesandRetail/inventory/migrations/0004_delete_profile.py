# Generated by Django 5.0.1 on 2024-03-18 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
