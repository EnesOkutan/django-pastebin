# Generated by Django 2.1.5 on 2019-02-05 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PasteSiteApp', '0007_auto_20190205_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paste',
            options={'ordering': ['-created_on']},
        ),
    ]
