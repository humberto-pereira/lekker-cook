# Generated by Django 3.2.22 on 2023-11-03 14:44

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_commentlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='carousel_image')),
                ('heading', models.CharField(max_length=250)),
                ('caption', models.TextField()),
            ],
        ),
    ]
