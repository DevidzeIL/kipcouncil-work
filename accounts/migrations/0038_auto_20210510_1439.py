# Generated by Django 3.2 on 2021-05-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20210510_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='photo',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='useraward',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
