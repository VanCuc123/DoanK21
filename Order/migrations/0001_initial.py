# Generated by Django 4.2.5 on 2024-07-17 07:45

import Order.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Coupon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=Order.models.generate_random_code, max_length=10, unique=True, verbose_name='Order Code')),
                ('customer', models.CharField(max_length=255, verbose_name='Customer Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('coupon_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Coupon.coupon', verbose_name='Coupon Code')),
            ],
        ),
    ]
