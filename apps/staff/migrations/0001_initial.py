# Generated by Django 2.2.3 on 2019-07-06 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persian_name', models.CharField(max_length=300)),
                ('english_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persian_name', models.CharField(max_length=300)),
                ('english_name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='staff_photos')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Event')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Role')),
            ],
        ),
    ]
