# Generated by Django 2.2.3 on 2019-08-05 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_event_english_poster'),
        ('gallery', '0008_auto_20190805_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='content.Event'),
            preserve_default=False,
        ),
    ]
