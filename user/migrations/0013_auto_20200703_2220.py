# Generated by Django 3.0.7 on 2020-07-03 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200703_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expirattion_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 22, 20, 33, 679076)),
        ),
    ]
