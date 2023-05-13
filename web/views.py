from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request, 'bookings/index.html')

def bookings(request):
    all_bookings = Booking.objects.all()
    context = {'bookings': all_bookings}
    return render(request, 'bookings/bookings.html', context)

def new_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = BookingForm()
    context = {'form': form}
    return render(request, 'bookings/new_booking.html', context)