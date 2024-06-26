from django.db import models
from django.utils.html import mark_safe


class MainSettings(models.Model):
    name = models.CharField( max_length=150)
    logo = models.ImageField( upload_to='company/')
    description = models.TextField( max_length=1000, default='', blank=True, null=True)

    email = models.EmailField( max_length=500, default='default@default.com', blank=True, null=True)
    phone = models.CharField( max_length=150, default='01099999', blank=True, null=True)

    facebook = models.URLField( max_length=500, blank=True, null=True)
    linkedin = models.URLField( max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'MainSettings'

    def logo_tag(self):
        return mark_safe(f'<img src="{self.logo.url}" width="150" height="70"/>')