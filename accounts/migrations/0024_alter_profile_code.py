# Generated by Django 5.0.7 on 2024-07-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_profile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='pmoclX6qjy8e4NM3iyYi', max_length=200, null=True),
        ),
    ]
