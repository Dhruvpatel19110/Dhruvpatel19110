# Generated by Django 4.0.1 on 2022-04-13 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0043_rename_name_wishlist_name1_remove_wishlist_upload_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
