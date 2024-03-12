# Generated by Django 4.0 on 2024-03-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
            ],
        ),
    ]
