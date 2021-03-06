# Generated by Django 3.1.3 on 2020-11-17 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=500, verbose_name='product')),
                ('date', models.DateField(verbose_name='order create date')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=500, verbose_name='last_name')),
                ('date_birthday', models.DateField(verbose_name='date of birth')),
                ('date_order', models.DateField(verbose_name='date of order')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to='izziapp.order', verbose_name='user_order')),
            ],
        ),
    ]
