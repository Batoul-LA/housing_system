from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BookingForm,PaymentForm
from .models import Booking, Payment,Room
from access.models import QR
from rest_framework import viewsets
from .serializers import RoomSerializer, BookingSerializer, PaymentSerializer

def index(request):
    return HttpResponse("App is working.")

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # توليد QR تلقائي مرتبط بالحجز
            QR.objects.create(booking=booking, code=f"booking:{booking.id}")
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/create_booking.html', {'form': form})

def booking_list(request):
    bookings = Booking.objects.select_related('student', 'room').prefetch_related('payments')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def add_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            return redirect('booking_list')
    else:
        form = PaymentForm()
    return render(request, 'booking/add_payment.html', {'form': form, 'booking': booking})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
