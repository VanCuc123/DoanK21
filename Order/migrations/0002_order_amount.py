# Generated by Django 4.2.5 on 2024-07-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='Amount'),
        ),
    ]
