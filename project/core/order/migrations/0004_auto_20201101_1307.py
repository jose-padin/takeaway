# Generated by Django 3.1.2 on 2020-11-01 13:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201101_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 13, 7, 47, 597608, tzinfo=utc), verbose_name='Date'),
        ),
    ]
