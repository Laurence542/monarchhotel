# Generated by Django 4.1.4 on 2023-08-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]