# Generated by Django 2.2.3 on 2019-08-05 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20190804_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='english_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='persian_name',
        ),
    ]
