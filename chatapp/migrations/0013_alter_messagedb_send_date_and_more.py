# Generated by Django 4.1.7 on 2023-04-28 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0012_alter_messagedb_send_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagedb',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 22, 21, 34, 666359)),
        ),
        migrations.AlterField(
            model_name='messagenofity',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 22, 21, 34, 667360)),
        ),
    ]
