# Generated by Django 5.0.3 on 2024-05-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0002_alter_vendor_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]