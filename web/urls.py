from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/new/', views.new_booking, name='new_booking'),
]