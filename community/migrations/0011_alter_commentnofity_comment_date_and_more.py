# Generated by Django 4.1.7 on 2023-04-24 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_alter_commentnofity_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentnofity',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 21, 12, 25, 425250)),
        ),
        migrations.AlterField(
            model_name='communitycomment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 21, 12, 25, 424249)),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 21, 12, 25, 424249)),
        ),
    ]