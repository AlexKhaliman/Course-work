# Generated by Django 2.2.5 on 2019-10-05 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='offers',
        ),
    ]
