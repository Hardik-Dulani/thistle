# Generated by Django 4.1.6 on 2023-03-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='cart',
            field=models.CharField(default='', max_length=5000),
        ),
    ]