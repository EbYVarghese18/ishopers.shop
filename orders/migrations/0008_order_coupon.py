# Generated by Django 4.1.2 on 2022-12-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_email_order_orderemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
