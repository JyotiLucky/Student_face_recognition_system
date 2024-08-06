# Generated by Django 5.0.7 on 2024-07-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('registration_id', models.CharField(max_length=20, unique=True)),
                ('branch', models.CharField(max_length=100)),
                ('face_encodings', models.JSONField()),
            ],
        ),
    ]
