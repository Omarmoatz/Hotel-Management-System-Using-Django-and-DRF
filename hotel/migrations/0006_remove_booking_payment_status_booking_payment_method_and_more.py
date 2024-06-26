# Generated by Django 5.0.3 on 2024-06-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_remove_roomtype_img_alter_booking_booking_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cach', 'cach'), ('visa', 'visa'), ('strip', 'strip'), ('paypal', 'paypal')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='max_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_code',
            field=models.CharField(blank=True, default='Lelpdbjnnc', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(blank=True, default='defaul_name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='subtitle',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=50),
        ),
    ]
