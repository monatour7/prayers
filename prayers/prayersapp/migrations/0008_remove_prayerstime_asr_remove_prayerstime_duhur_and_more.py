# Generated by Django 4.1 on 2022-08-28 20:56

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prayersapp', '0007_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayerstime',
            name='asr',
        ),
        migrations.RemoveField(
            model_name='prayerstime',
            name='duhur',
        ),
        migrations.RemoveField(
            model_name='prayerstime',
            name='fajr',
        ),
        migrations.RemoveField(
            model_name='prayerstime',
            name='imsak',
        ),
        migrations.RemoveField(
            model_name='prayerstime',
            name='isha',
        ),
        migrations.RemoveField(
            model_name='prayerstime',
            name='maghrib',
        ),
        migrations.RemoveField(
            model_name='prayerstime',
            name='sunrise',
        ),
        migrations.AddField(
            model_name='prayerstime',
            name='date',
            field=models.DateField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='prayerstime',
            name='prayerTimes',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]