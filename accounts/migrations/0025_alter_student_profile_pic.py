# Generated by Django 3.2 on 2021-05-03 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20210504_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to=''),
        ),
    ]
