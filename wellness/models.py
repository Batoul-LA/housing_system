from django.db import models
from users.models import Employee
from booking.models import Room 
from django.core.exceptions import ValidationError

class WellnessCheck(models.Model):
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="wellness_checks")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="wellness_checks")
    inspection_date = models.DateField()
    
    security_notes = models.TextField(blank=True, null=True)
    maintenance_notes = models.TextField(blank=True, null=True)

    needs_maintenance = models.BooleanField(default=False)
    follow_up_required = models.BooleanField(default=False)

    def __str__(self):
        return f"Inspection by {self.employee.full_name} in Room {self.room.number} on {self.inspection_date}"

    def clean(self):
        super().clean()
        if self.needs_maintenance and not self.maintenance_notes:
            raise ValidationError("يرجى إدخال ملاحظات الصيانة عند تحديد أن الغرفة تحتاج لصيانة.")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['room', 'inspection_date'], name='unique_room_inspection_per_day')
        ]
