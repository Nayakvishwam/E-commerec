# Generated by Django 3.2.4 on 2021-12-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_remove_orderupdate_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="productdetails",
            name="quantities",
            field=models.IntegerField(default=0),
        ),
    ]