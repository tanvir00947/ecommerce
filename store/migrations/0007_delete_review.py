# Generated by Django 4.2.6 on 2023-11-20 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_orderitem_product_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
