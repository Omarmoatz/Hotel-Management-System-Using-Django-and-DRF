# Generated by Django 5.0.7 on 2024-07-31 17:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(blank=True, choices=[('cach', 'cach'), ('visa', 'visa'), ('strip', 'strip'), ('paypal', 'paypal')], max_length=50, null=True)),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(blank=True, max_length=900, null=True)),
                ('before_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('money_saved', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('check_in_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('check_out_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('total_days', models.PositiveIntegerField(blank=True, null=True)),
                ('num_adults', models.PositiveIntegerField(blank=True, null=True)),
                ('num_children', models.PositiveIntegerField(blank=True, null=True)),
                ('check_in', models.BooleanField(default=False)),
                ('check_out', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('booking_code', models.CharField(blank=True, default='Nf8a5OTZI5', max_length=500, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_booked', to='hotel.hotel')),
                ('room', models.ManyToManyField(to='hotel.room')),
                ('room_type', models.ManyToManyField(to='hotel.roomtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_user', to=settings.AUTH_USER_MODEL)),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.coupon')),
            ],
        ),
    ]
