from django.db import models
from booking.models import Room  
from django.core.exceptions import ValidationError

class Camera(models.Model):
    STATUS_CHOICES = [
        ('active', 'فعالة'),
        ('inactive', 'غير فعالة'),
        ('maintenance', 'تحت الصيانة'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="cameras")
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    installation_date = models.DateField()

    def __str__(self):
        return f"Camera in {self.room.number} - {self.location}"


class CameraRecord(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name="records")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    file_path = models.FileField(upload_to='camera_records/')
    size = models.IntegerField(help_text="Size in MB")
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='camera_records/videos/', blank=True, null=True)

    def clean(self):
        super().clean()
        if self.end_time <= self.start_time:
            raise ValidationError("تاريخ نهاية التسجيل يجب أن يكون بعد تاريخ البداية.")
    
    def __str__(self):
        return f"Record {self.id} from Camera {self.camera.id}"

    class Meta:
        ordering = ['-start_time']   # أحدث تسجيل يظهر أولاً
