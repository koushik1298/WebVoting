# Generated by Django 2.1.5 on 2019-04-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='model_pic',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
