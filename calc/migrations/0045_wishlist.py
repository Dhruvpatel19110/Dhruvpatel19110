# Generated by Django 4.0.4 on 2022-04-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0044_delete_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('HP', models.IntegerField(blank=True, null=True)),
                ('Manufacturingyear', models.IntegerField(blank=True, null=True)),
                ('Regno', models.CharField(blank=True, max_length=10, null=True)),
                ('RC', models.CharField(blank=True, max_length=3, null=True)),
                ('Hours', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
