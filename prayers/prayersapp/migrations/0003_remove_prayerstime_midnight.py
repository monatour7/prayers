# Generated by Django 4.1 on 2022-08-24 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prayersapp', '0002_prayerstime_midnight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayerstime',
            name='midnight',
        ),
    ]
