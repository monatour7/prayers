# Generated by Django 4.1 on 2022-08-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayersapp', '0003_remove_prayerstime_midnight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
    ]
