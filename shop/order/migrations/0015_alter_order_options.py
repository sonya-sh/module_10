# Generated by Django 4.0.2 on 2022-03-20 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_order_id_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_on',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
