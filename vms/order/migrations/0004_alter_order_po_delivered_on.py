# Generated by Django 5.0.3 on 2024-05-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_order_po_delivered_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="po_delivered_on",
            field=models.DateTimeField(
                blank=True,
                help_text="actual time when the PO is sucessfully delivered",
                null=True,
            ),
        ),
    ]