# Generated by Django 4.1.7 on 2023-08-24 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_visitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='user_agent',
        ),
    ]
