# Generated by Django 3.2.9 on 2021-12-07 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patientCreateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
