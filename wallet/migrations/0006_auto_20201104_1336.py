# Generated by Django 3.1.2 on 2020-11-04 08:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 4, 8, 6, 39, 155747, tzinfo=utc)),
        ),
    ]
