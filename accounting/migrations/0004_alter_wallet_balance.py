# Generated by Django 4.2.6 on 2023-11-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_alter_wallet_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.IntegerField(verbose_name='Баланс'),
        ),
    ]
