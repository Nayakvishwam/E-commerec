# Generated by Django 3.2.5 on 2022-01-31 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_productdetails_d'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='d',
        ),
    ]