# Generated by Django 4.1.6 on 2023-03-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_orders_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_id',
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_ref',
            field=models.CharField(default='', max_length=25, primary_key=True, serialize=False),
        ),
    ]
