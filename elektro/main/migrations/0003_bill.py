# Generated by Django 4.2.20 on 2025-05-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tariff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_number', models.CharField(max_length=50)),
                ('day_kwh', models.IntegerField()),
                ('night_kwh', models.IntegerField()),
                ('day_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('night_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
