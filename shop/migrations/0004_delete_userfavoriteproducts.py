# Generated by Django 4.2.5 on 2023-09-13 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_userfavoriteproducts_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFavoriteProducts',
        ),
    ]