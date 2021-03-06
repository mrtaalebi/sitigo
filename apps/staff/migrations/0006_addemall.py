# Generated by Django 2.2.3 on 2019-08-06 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_fileupload_language'),
        ('staff', '0005_auto_20190805_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddEmAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_csv', models.FileField(upload_to='addemall')),
                ('role_csv', models.FileField(upload_to='addemall')),
                ('data_csv', models.FileField(upload_to='addemall')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Event')),
            ],
        ),
    ]
