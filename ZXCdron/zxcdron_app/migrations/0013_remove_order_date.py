# Generated by Django 4.2.6 on 2023-10-27 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zxcdron_app', '0012_order_date_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
    ]
