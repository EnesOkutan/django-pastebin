# Generated by Django 2.1.5 on 2019-02-05 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PasteSiteApp', '0003_auto_20190205_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 2, 5, 12, 36, 29, 273415, tzinfo=utc)),
        ),
    ]
