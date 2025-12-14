from django.db import models
from users.models import Student

class QR(models.Model):
    booking = models.OneToOneField('booking.Booking', on_delete=models.CASCADE, related_name='qr')
    code = models.CharField(max_length=255, unique=True)  # القيمة النصية للـ QR
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR for booking {self.booking.id}"



class AccessLog(models.Model):
    qr = models.ForeignKey(QR, on_delete=models.CASCADE)
    employee = models.ForeignKey('users.Employee', on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('in', 'In'), ('out', 'Out')])

    def __str__(self):
        return f"{self.employee} scanned {self.qr} at {self.timestamp}"

