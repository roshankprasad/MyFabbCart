# Generated by Django 2.2.4 on 2019-10-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produce_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
