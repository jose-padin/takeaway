# Generated by Django 3.1 on 2020-12-05 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20201205_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 5, 14, 25, 25, 773748, tzinfo=utc), verbose_name='Date'),
        ),
    ]