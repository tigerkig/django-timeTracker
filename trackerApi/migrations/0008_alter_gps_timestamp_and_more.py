# Generated by Django 4.0.3 on 2022-11-05 00:12

from django.db import migrations
import django_postgres_timestamp_without_tz


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApi', '0007_alter_gps_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='timestamp',
            field=django_postgres_timestamp_without_tz.DateTimeWithoutTZField(blank=True, default='2022-11-05 00:12:48'),
        ),
        migrations.AlterField(
            model_name='payroll_time_period',
            name='start_time',
            field=django_postgres_timestamp_without_tz.DateTimeWithoutTZField(default='2022-11-05 00:12:48', null=True),
        ),
        migrations.AlterField(
            model_name='work_time_period',
            name='start_time',
            field=django_postgres_timestamp_without_tz.DateTimeWithoutTZField(blank=True, default='2022-11-05 00:12:48'),
        ),
    ]
