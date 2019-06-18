# Generated by Django 2.1 on 2019-05-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('no_participant', models.IntegerField()),
                ('event_level', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('prerequisite', models.TextField(max_length=1500)),
                ('facility', models.CharField(max_length=100)),
                ('event_detail_docs', models.FileField(upload_to='event_details_docs')),
            ],
        ),
    ]
