# Generated by Django 2.0.1 on 2018-01-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_auto_20180116_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='picture',
            field=models.ImageField(blank=True, upload_to='link_images'),
        ),
    ]