# Generated by Django 4.2.6 on 2023-11-20 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='default review')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
