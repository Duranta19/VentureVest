# Generated by Django 4.1.7 on 2023-04-20 08:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateTimeField(default=datetime.datetime(2023, 4, 20, 14, 49, 43, 323780))),
                ('msgg', models.CharField(max_length=1000)),
                ('r_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_id', to='auths.auts')),
                ('s_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s_id', to='auths.auts')),
            ],
        ),
    ]
