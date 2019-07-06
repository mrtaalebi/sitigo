# Generated by Django 2.2.2 on 2019-07-06 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_page_slideshow')),
                ('homePage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_page_image', to='intro.HomePage')),
            ],
        ),
    ]
