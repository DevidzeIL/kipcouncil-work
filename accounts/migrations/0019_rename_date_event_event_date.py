# Generated by Django 3.2 on 2021-05-03 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210503_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date_event',
            new_name='date',
        ),
    ]
