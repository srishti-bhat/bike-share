# Generated by Django 3.2.8 on 2021-11-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeoperator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='operator',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]