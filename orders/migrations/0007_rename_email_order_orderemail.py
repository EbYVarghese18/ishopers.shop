# Generated by Django 4.1.2 on 2022-12-24 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='orderemail',
        ),
    ]