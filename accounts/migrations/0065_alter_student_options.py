# Generated by Django 3.2 on 2021-06-06 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0064_member_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['fio']},
        ),
    ]
