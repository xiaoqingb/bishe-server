# Generated by Django 2.2.8 on 2021-03-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210317_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostandfound',
            name='lost_type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='lostandfound',
            name='tell',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lostandfound',
            name='id',
            field=models.AutoField(default='', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lostandfound',
            name='type',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lostandfound',
            name='user_id',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='openid',
            field=models.CharField(default='', max_length=200),
        ),
    ]