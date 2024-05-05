# Generated by Django 5.0.3 on 2024-05-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "performance_history",
            "0002_alter_historicalperformance_fulfillment_rate_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalperformance",
            name="average_response_time",
            field=models.FloatField(
                blank=True,
                help_text="Historical record of the average response time in (hr:mm).",
                null=True,
            ),
        ),
    ]