from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, TimeFramedModel

from apps.users.models import User
from apps.hotel.models import Hotel, Room, RoomType

class Booking(TimeStampedModel):
    class PAYMENT_METHOD(models.TextChoices):
        CASH = 'cash', _('Cash')
        VISA = 'visa', _('Visa')
        STRIPE = 'stripe', _('Stripe')
        PAYPAL = 'paypal', _('Paypal')

    user = models.ForeignKey(User, related_name='booked_user', on_delete=models.CASCADE)
    payment_method = models.CharField( max_length=10, choices=PAYMENT_METHOD.choices, blank=True, null=True)

    full_name = models.CharField( max_length=500, blank=True, null=True)
    phone = models.CharField( max_length=500, blank=True, null=True)
    email = models.EmailField( max_length=900, blank=True, null=True)

    hotel = models.ForeignKey( Hotel, related_name='hotel_booked', on_delete=models.CASCADE)
    room_type = models.ManyToManyField( RoomType )
    room =  models.ManyToManyField( Room )
    before_discount = models.DecimalField( max_digits=9, decimal_places=2, blank=True, null=True)
    total = models.DecimalField( max_digits=9, decimal_places=2, blank=True, null=True)
    money_saved = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True)
    
    check_in_date = models.DateField( default=timezone.now, blank=True, null=True)
    check_out_date = models.DateField( default=timezone.now, blank=True, null=True)
    total_days = models.PositiveIntegerField(blank=True, null=True)
    num_adults = models.PositiveIntegerField(blank=True, null=True)
    num_children = models.PositiveIntegerField(blank=True, null=True)

    check_in = models.BooleanField(default=False)
    check_out = models.BooleanField(default=False)
    
    booking_code = models.CharField( max_length=500, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'booking{self.id} for {str(self.user)}'
    
    def save(self, *args, **kwargs):
       self.booking_code = get_random_string(10)
       return super().save(*args, **kwargs) 
       
    class Meta:
        ordering = ['-created']
    

class Coupon(TimeFramedModel):
    code = models.CharField( max_length=100, blank=True, null=True)
    discount = models.PositiveIntegerField( blank=True, null=True)
    quantity = models.PositiveIntegerField( blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.discount}% off"
    
    def save(self, *args, **kwargs):
        if not self.end:
            week = timedelta(days=7)
            self.end = self.start + week

        if not self.code:
            self.code = get_random_string(10)
            
        return super(Coupon, self).save(*args, **kwargs) 

    class Meta:
        ordering = ['-start']