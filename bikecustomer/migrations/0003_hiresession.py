# Generated by Django 3.2.1 on 2021-10-02 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bikecustomer', '0002_auto_20211002_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiresession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.IntegerField()),
                ('customer_id', models.CharField(max_length=100)),
                ('start_depot', models.CharField(max_length=40)),
                ('end_depot', models.CharField(max_length=40)),
                ('bike_id', models.CharField(max_length=100)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'sessions',
            },
        ),
    ]
