# Generated by Django 4.1.7 on 2023-06-16 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_addrooms_delete_rooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addrooms',
            old_name='image',
            new_name='image1',
        ),
    ]
