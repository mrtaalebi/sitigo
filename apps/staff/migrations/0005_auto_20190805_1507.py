# Generated by Django 2.2.3 on 2019-08-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20190805_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='english_firstname',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='english_lastname',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='persian_firstname',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='persian_lastname',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
