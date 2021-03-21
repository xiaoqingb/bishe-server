# Generated by Django 2.2.8 on 2021-03-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210321_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(default='', max_length=200)),
                ('content_id', models.CharField(default='', max_length=200)),
                ('user_id', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'user_favorite',
            },
        ),
    ]
