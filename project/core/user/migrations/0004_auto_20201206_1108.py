# Generated by Django 3.1 on 2020-12-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201206_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
