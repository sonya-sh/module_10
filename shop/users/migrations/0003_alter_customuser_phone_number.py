# Generated by Django 4.0.2 on 2022-03-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_email_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='888', max_length=255, verbose_name='Номер телефона'),
        ),
    ]
