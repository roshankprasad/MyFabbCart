# Generated by Django 2.2.4 on 2019-10-19 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191019_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Produce_name',
            new_name='product_name',
        ),
    ]