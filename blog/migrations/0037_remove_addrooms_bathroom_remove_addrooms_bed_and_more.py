# Generated by Django 4.1.4 on 2023-08-25 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_visitor_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addrooms',
            name='bathroom',
        ),
        migrations.RemoveField(
            model_name='addrooms',
            name='bed',
        ),
        migrations.RemoveField(
            model_name='addrooms',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='addrooms',
            name='price',
        ),
        migrations.RemoveField(
            model_name='addrooms',
            name='roomsleft',
        ),
    ]
