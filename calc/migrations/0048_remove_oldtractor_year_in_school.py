# Generated by Django 4.0.1 on 2022-04-15 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0047_oldtractor_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldtractor',
            name='year_in_school',
        ),
    ]
