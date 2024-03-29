# Generated by Django 5.0.2 on 2024-02-09 19:05

import cloudinary.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('thumbernail', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
                ('content', models.TextField()),
                ('time_read', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
