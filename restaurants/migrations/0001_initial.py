# Generated by Django 2.1.5 on 2019-10-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restuarant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=105)),
                ('description', models.TextField()),
                ('opening_time', models.CharField(max_length=5)),
                ('closing_time', models.CharField(max_length=5)),
            ],
        ),
    ]
