# Generated by Django 2.1.5 on 2019-02-04 21:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PasteSiteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 2, 4, 21, 48, 38, 524360, tzinfo=utc)),
        ),
    ]