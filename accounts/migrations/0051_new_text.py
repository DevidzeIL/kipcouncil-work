# Generated by Django 3.2 on 2021-05-20 12:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_auto_20210520_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, null=True),
        ),
    ]
