# Generated by Django 4.1.7 on 2023-04-24 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_alter_messagedb_send_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagedb',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 20, 45, 30, 911973)),
        ),
    ]