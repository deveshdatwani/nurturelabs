# Generated by Django 3.2 on 2021-05-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0004_rename_advisorcalls_calls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='photo_url',
            field=models.CharField(max_length=200),
        ),
    ]