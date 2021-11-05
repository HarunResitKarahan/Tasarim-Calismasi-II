# Generated by Django 3.2.9 on 2021-11-05 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientID', models.AutoField(primary_key=True, serialize=False)),
                ('patientName', models.CharField(max_length=200)),
                ('patientSurname', models.CharField(max_length=200)),
                ('patientEmail', models.CharField(max_length=200)),
                ('patientCreateTime', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
