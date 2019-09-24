# Generated by Django 2.2.5 on 2019-09-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20190924_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='comments',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('Looking for executor', 'looking_for_executor'), ('In process', 'in_process'), ('Done', 'done')], max_length=30),
        ),
    ]
