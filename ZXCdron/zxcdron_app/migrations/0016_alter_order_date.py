# Generated by Django 4.2.6 on 2023-10-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxcdron_app', '0015_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default='1111-11-11 11:11'),
        ),
    ]
