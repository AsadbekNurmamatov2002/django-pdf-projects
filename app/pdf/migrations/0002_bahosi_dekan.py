# Generated by Django 5.0.6 on 2024-06-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bahosi',
            name='dekan',
            field=models.CharField(blank=True, max_length=25, verbose_name='Fan krediti'),
        ),
    ]
