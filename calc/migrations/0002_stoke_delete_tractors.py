# Generated by Django 4.0.1 on 2022-03-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stoke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=1024)),
            ],
        ),
        migrations.DeleteModel(
            name='Tractors',
        ),
    ]
