# Generated by Django 4.0.1 on 2022-04-29 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0065_remove_oldtractor_engine_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldtractor',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='oldtractor',
            name='Min_Prize',
        ),
    ]
