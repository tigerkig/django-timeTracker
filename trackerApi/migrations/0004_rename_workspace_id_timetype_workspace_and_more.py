# Generated by Django 4.0.3 on 2022-11-04 16:53

from django.db import migrations
import django_postgres_timestamp_without_tz


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApi', '0003_remove_timetype_workspaces_id_timetype_workspace_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetype',
            old_name='workspace_id',
            new_name='workspace',
        ),
        migrations.AlterField(
            model_name='gps',
            name='timestamp',
            field=django_postgres_timestamp_without_tz.DateTimeWithoutTZField(blank=True, default='2022-11-04 16:53:42'),
        ),
        migrations.AlterField(
            model_name='payroll_time_period',
            name='start_time',
            field=django_postgres_timestamp_without_tz.DateTimeWithoutTZField(default='2022-11-04 16:53:42', null=True),
        ),
        migrations.AlterField(
            model_name='work_time_period',
            name='start_time',
            field=django_postgres_timestamp_without_tz.DateTimeWithoutTZField(blank=True, default='2022-11-04 16:53:42'),
        ),
    ]
