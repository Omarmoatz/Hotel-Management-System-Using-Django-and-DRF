# Generated by Django 5.0.4 on 2024-05-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_code_profile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='gYDjhChyVu3fLdGKZPWt', max_length=200, null=True),
        ),
    ]
