# Generated by Django 4.2.5 on 2024-07-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='media/images/', verbose_name='Image'),
        ),
    ]