# Generated by Django 2.2.8 on 2021-03-21 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lostandfound',
            old_name='published',
            new_name='publish_status',
        ),
    ]
