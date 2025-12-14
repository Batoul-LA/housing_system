from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, EmployeeForm
from django.views.generic.edit import CreateView
from .models import Student
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Student, Employee
from .serializers import StudentSerializer, EmployeeSerializer

# صفحة رئيسية للتطبيق (اسم أوضح بدل index)
def users_home(request):
    return HttpResponse("Users app is working.")

@login_required
def redirect_after_login(request):
    user = request.user

    if hasattr(user, 'student'):
        return redirect('student_dashboard')  # إذا طالب → واجهة الطالب
    elif hasattr(user, 'employee'):
        return redirect('employee_dashboard')  # إذا موظف → واجهة الموظف
    else:
        # بدل 'home' غير المعروفة، رجع للمسار الرئيسي لتطبيق users
        return redirect('users-home')

@login_required
def student_dashboard(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return JsonResponse({"message": "تم تسجيل بيانات الطالب بنجاح ✅"}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"message": "يرجى استخدام POST فقط"}, status=405)

@login_required
def employee_dashboard(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            return JsonResponse({"message": "تم تسجيل بيانات الموظف بنجاح ✅"}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"message": "يرجى استخدام POST فقط"}, status=405)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student_form.html'
    success_url = reverse_lazy('student_dashboard')

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    