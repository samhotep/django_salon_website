# Generated by Django 2.0.1 on 2018-01-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0011_auto_20180117_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
    ]