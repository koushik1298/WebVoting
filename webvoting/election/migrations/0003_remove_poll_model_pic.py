# Generated by Django 2.1.5 on 2019-04-25 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_poll_model_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='model_pic',
        ),
    ]