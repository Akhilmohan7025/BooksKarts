# Generated by Django 4.0.2 on 2022-02-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_carts_status_my_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_orders',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='carts',
            name='status',
            field=models.CharField(choices=[('order_placed', 'order_placed'), ('incart', 'incart'), ('cancel', 'cancel')], default='incart', max_length=120),
        ),
        migrations.AlterField(
            model_name='my_orders',
            name='excepted_delivery_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='my_orders',
            name='status',
            field=models.CharField(choices=[('Intransit', 'Intransit'), ('delivered', 'delivered'), ('order_placed', 'order_placed'), ('Dispatched', 'Dispatched'), ('cancel', 'cancel')], default='order_placed', max_length=120),
        ),
    ]
