# Generated by Django 4.0.1 on 2022-03-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0027_remove_oldtractor_desto_oldtractor_yearo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
