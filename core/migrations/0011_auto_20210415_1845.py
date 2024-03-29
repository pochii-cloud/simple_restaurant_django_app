# Generated by Django 3.1.7 on 2021-04-15 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_order_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='Food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.food'),
        ),
    ]
