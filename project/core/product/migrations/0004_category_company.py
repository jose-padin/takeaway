# Generated by Django 3.1 on 2020-11-06 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20201106_0822'),
        ('product', '0003_auto_20201101_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='company.company'),
            preserve_default=False,
        ),
    ]
