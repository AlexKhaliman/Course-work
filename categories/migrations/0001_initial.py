# Generated by Django 2.2.5 on 2019-10-05 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static/img/')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('posted_time', models.DateTimeField(auto_now_add=True)),
                ('invited_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited_to', to=settings.AUTH_USER_MODEL)),
                ('suggested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggested_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('Looking for executor', 'looking_for_executor'), ('In process', 'in_process'), ('Done', 'done')], default='looking for executor', max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.Categories')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('offers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Offers')),
            ],
        ),
    ]
