from django.urls import path
from . import views
from .views import StudentCreateView
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, EmployeeViewSet

urlpatterns = [
    path('', views.users_home, name='users-home'),
    path('after-login/', views.redirect_after_login, name='redirect-after-login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('student/', StudentCreateView.as_view(), name='student_create'), 
]
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls