# Generated by Django 2.2.5 on 2019-10-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_auto_20191006_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='from_whom',
            field=models.PositiveIntegerField(),
        ),
    ]