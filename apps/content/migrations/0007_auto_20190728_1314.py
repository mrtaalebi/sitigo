# Generated by Django 2.2.3 on 2019-07-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20190718_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='content.ImageUpload'),
        ),
    ]
