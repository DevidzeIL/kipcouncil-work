# Generated by Django 3.2 on 2021-05-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_listdirection_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='listdirection',
            name='status',
            field=models.CharField(blank=True, choices=[('Участник', 'Участник'), ('Правление', 'Правление')], max_length=200, null=True),
        ),
    ]
