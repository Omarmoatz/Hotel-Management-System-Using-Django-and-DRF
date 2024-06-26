from django.urls import path

from . import views

app_name = 'hotel'

  #   hotels/
urlpatterns = [
    path('', views.HotelList.as_view(), name='hotel_list' ),
    path('<slug>/', views.HotelDetail.as_view(), name='hotel_detail' ),
    path('book_hotel/', views.BookingHotel.as_view(), name='book_hotel' ),
]
