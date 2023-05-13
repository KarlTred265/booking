from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=50, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    date = models.DateField(verbose_name="Booking Date")
    time = models.CharField(max_length=10, choices=[(f"{i:02d}:00", f"{i:02d}:00") for i in range(6, 23)],
                            verbose_name="Booking Time")
    booking_ref = models.CharField(max_length=10, verbose_name="Booking Reference")
    num_of_guests = models.IntegerField(verbose_name="Number of Guests")
    message = models.TextField(blank=True, verbose_name="Additional Message")

    class Meta:
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f'{self.name} on {self.date} at {self.time}'