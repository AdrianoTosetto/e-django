# Generated by Django 2.1.dev20170922165119 on 2017-11-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_appuser_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='appmessage',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
