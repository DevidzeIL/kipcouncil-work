# Generated by Django 3.2 on 2021-05-20 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_new_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='common_text',
        ),
        migrations.RemoveField(
            model_name='new',
            name='date_performance',
        ),
        migrations.RemoveField(
            model_name='new',
            name='third_text',
        ),
    ]
