# Generated by Django 3.2.9 on 2021-12-16 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentApp', '0004_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointmentTime',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.schedule'),
        ),
    ]