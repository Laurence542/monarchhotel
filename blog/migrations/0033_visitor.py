# Generated by Django 4.1.7 on 2023-08-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_delete_visit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
