# Generated by Django 4.1.2 on 2022-12-20 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_rename_code_coupon_coupon_code_remove_coupon_active_and_more'),
        ('cart', '0003_cartitem_variations'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupon.coupon'),
        ),
    ]