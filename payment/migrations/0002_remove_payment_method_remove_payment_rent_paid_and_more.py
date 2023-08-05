# Generated by Django 4.2.3 on 2023-08-05 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='method',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='rent_paid',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='rent_unpaid',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.TextField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]
