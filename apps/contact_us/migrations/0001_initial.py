# Generated by Django 2.2.2 on 2019-07-03 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(default='ran, Islamic Republic of', max_length=50)),
                ('school_uni', models.CharField(max_length=50)),
                ('study_grade', models.CharField(choices=[('middle school', 'middle school'), ('high school', 'high school'), ('university', 'university')], max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format with region code: '+999999999'. Up to 18 digits allowed.", regex='^\\+?1?\\d{9,19}$')])),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
    ]
