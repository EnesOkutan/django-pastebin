# Generated by Django 2.1.5 on 2019-02-05 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PasteSiteApp', '0002_auto_20190205_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 2, 5, 11, 27, 10, 348092, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='language',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='paste',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]