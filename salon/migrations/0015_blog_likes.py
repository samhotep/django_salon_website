# Generated by Django 2.0.1 on 2018-02-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0014_auto_20180118_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
