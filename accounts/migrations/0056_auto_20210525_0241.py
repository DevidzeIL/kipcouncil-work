# Generated by Django 3.2 on 2021-05-24 23:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0055_remove_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='common_text',
        ),
        migrations.AddField(
            model_name='about',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='goals',
            field=ckeditor.fields.RichTextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='main_text',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='result',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='main_text',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='More',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('goals', ckeditor.fields.RichTextField(blank=True, max_length=200, null=True)),
                ('main_text', ckeditor.fields.RichTextField(blank=True, max_length=300, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('tags', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.tag')),
            ],
        ),
    ]
