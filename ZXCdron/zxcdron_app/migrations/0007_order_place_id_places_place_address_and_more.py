# Generated by Django 4.2.6 on 2023-10-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxcdron_app', '0006_remove_order_date_and_time_alter_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='place_id',
            field=models.CharField(default='test', max_length=5),
        ),
        migrations.AddField(
            model_name='places',
            name='place_address',
            field=models.CharField(default='test', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='test', max_length=200),
        ),
    ]
