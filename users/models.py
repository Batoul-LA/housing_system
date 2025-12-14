from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    account_type = [
        ('student', 'Student'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=10, choices=account_type,blank=False, null=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20, unique=True)  # رقم السكن الداخلي
    university_id = models.CharField(max_length=20, unique=True)  # الرقم الجامعي الرسمي
    faculty = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    year = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=[('مستجد', 'مستجد'), ('راسب', 'راسب')]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.university_id})"




class Employee(models.Model):
    ROLE_CHOICES = [
        ('admin', 'مدير'),
        ('security', 'أمن'),
        ('maintenance', 'صيانة'),
    ]
    BLOOD_CHOICES = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
]
    employee_id = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(default=30)
    blood_type = models.CharField(max_length=3, choices=BLOOD_CHOICES, default='O+')
    family_status = models.CharField(max_length=20,default='single')
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
