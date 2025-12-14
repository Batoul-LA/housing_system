from django.db import models
from users.models import Student
from django.core.exceptions import ValidationError

class Room(models.Model):
   ROOM_TYPE_CHOICES = [
    ('single', 'Single'),
    ('double', 'Double'),
    ('triple', 'Triple'),
]

   ROOM_STATUS_CHOICES = [
    ('available', 'متاحة'),
    ('occupied', 'مشغولة'),
    ('maintenance', 'صيانة'),
]
   status = models.CharField(max_length=20, choices=ROOM_STATUS_CHOICES, default='available')
   number=models.CharField(max_length=20, unique=True)
   type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='double')
   notes = models.TextField(blank=True, null=True)

   def __str__(self):
        return f"Room {self.number}({self.get_status_display()})"
   

class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
    ('active', 'نشطة'),
    ('ended', 'منتهية'),
    ('cancelled', 'ملغاة'),
   ]

    PAYMENT_STATUS_CHOICES = [
    ('unpaid', 'غير مدفوعة'),
    ('partial', 'مدفوعة جزئياً'),
    ('paid', 'مدفوعة'),
   ]

    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='bookings')
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default='active')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        super().clean()
        if self.end_date < self.start_date:
            raise ValidationError("تاريخ الانتهاء يجب أن يكون بعد أو يساوي تاريخ البداية.")

    def __str__(self):
        return f"Booking {self.id} - {self.student}"

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'نقدي'),
        ('card', 'بطاقة'),
        ('online', 'دفع إلكتروني'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    paid_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
    max_length=10,
    choices=[
        ('pending', 'قيد الانتظار'),
        ('paid', 'مدفوع'),
    ]
    )

    def __str__(self):
        return f"Payment {self.amount} for Booking {self.booking.id}"

