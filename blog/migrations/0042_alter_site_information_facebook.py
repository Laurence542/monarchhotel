# Generated by Django 4.1.4 on 2023-08-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_site_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_information',
            name='facebook',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
