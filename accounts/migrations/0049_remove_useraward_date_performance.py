# Generated by Django 3.2 on 2021-05-19 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_auto_20210519_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraward',
            name='date_performance',
        ),
    ]