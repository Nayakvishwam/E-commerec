# Generated by Django 3.2.4 on 2021-10-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="productdetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Product_name", models.CharField(max_length=100)),
                ("Product_desc", models.CharField(max_length=10000)),
                ("product_date", models.DateField()),
            ],
        ),
    ]
