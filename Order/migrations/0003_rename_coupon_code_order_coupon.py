# Generated by Django 4.2.5 on 2024-07-17 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_order_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='coupon_code',
            new_name='coupon',
        ),
    ]