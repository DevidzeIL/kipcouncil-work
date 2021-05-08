# Generated by Django 3.2 on 2021-05-08 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20210509_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='tags',
        ),
        migrations.AddField(
            model_name='about',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.tag'),
        ),
        migrations.RemoveField(
            model_name='new',
            name='tags',
        ),
        migrations.AddField(
            model_name='new',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.tag'),
        ),
    ]
