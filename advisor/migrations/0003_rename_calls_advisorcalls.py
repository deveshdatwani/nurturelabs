# Generated by Django 3.2 on 2021-05-03 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_calls'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Calls',
            new_name='AdvisorCalls',
        ),
    ]