# Generated by Django 3.2 on 2021-06-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20210601_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
