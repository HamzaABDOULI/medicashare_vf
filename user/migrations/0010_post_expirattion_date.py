# Generated by Django 3.0.7 on 2020-06-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_notification_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='expirattion_date',
            field=models.DateField(null=True),
        ),
    ]
