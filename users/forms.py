from django import forms
from .models import Student, Employee

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'father_name',
            'student_id',
            'university_id',
            'faculty',
            'specialization',
            'year',
            'status'
        ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'employee_id',   # رقم الموظف
            'phone',         # رقم الهاتف
            'email',         # البريد الإلكتروني
            'full_name',
            'age',
            'blood_type',
            'family_status',
            'role'
        ]
