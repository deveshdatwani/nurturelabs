# Generated by Django 3.2 on 2021-05-04 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0006_auto_20210504_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calls',
            old_name='advisorid',
            new_name='advisor',
        ),
        migrations.RenameField(
            model_name='calls',
            old_name='userid',
            new_name='user',
        ),
    ]
