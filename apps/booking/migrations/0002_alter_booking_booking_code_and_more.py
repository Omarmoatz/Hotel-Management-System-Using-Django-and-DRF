# Generated by Django 5.0.7 on 2024-09-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_code',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('visa', 'Visa'), ('stripe', 'Stripe'), ('paypal', 'Paypal')], max_length=10, null=True),
        ),
    ]