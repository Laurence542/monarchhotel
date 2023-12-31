# Generated by Django 4.1.7 on 2023-06-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_information_zip_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='address_info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='city_info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='email_info',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='state_info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='zip_info',
            field=models.CharField(max_length=100),
        ),
    ]
