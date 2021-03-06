# Generated by Django 3.2 on 2021-05-08 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_remove_member_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocsName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='docscouncil',
            name='direction',
        ),
        migrations.AddField(
            model_name='docscouncil',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Tag'),
        ),
        migrations.AddField(
            model_name='new',
            name='date_performance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='docscollege',
            name='cource',
            field=models.CharField(blank=True, choices=[('1 курс', '1 курс'), ('2 курс', '2 курс'), ('3 курс', '3 курс'), ('4 курс', '4 курс')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.event'),
        ),
        migrations.AlterField(
            model_name='company',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.specialty'),
        ),
        migrations.AlterField(
            model_name='docscollege',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.docsname'),
        ),
        migrations.AlterField(
            model_name='docscollege',
            name='specialty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.specialty'),
        ),
        migrations.AlterField(
            model_name='docscouncil',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.docsname'),
        ),
    ]
