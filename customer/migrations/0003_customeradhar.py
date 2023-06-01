# Generated by Django 4.2.1 on 2023-05-27 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_customeraddress_delete_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAdhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_number', models.IntegerField(blank=True, null=True)),
                ('adhar_name', models.CharField(blank=True, max_length=15, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
