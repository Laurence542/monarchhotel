# Generated by Django 4.1.7 on 2023-08-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_remove_visitor_user_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='cookie_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
