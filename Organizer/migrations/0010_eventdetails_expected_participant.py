# Generated by Django 2.1 on 2019-06-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0009_auto_20190614_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='expected_participant',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]