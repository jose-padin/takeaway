# Generated by Django 3.1.2 on 2020-11-01 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 11, 17, 35, 162963, tzinfo=utc), verbose_name='Date'),
        ),
    ]
