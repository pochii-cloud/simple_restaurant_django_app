# Generated by Django 3.1.7 on 2021-04-15 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210415_1845'),
    ]

    operations = [
        migrations.DeleteModel(
            name='send',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'contacts'},
        ),
    ]
