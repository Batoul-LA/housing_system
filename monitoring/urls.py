from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CameraViewSet, CameraRecordViewSet

app_name = 'monitoring'

urlpatterns = [
    # الصفحة الرئيسية للتطبيق (ممكن نربطها بقائمة الكاميرات)
    path('', views.camera_list, name='monitoring-home'),

    # إدارة الكاميرات
    path('cameras/add/', views.add_camera, name='add_camera'),
    path('cameras/', views.camera_list, name='camera_list'),

    # إدارة التسجيلات
    path('records/', views.record_list, name='record_list'),
    path('records/<int:pk>/', views.record_detail, name='record_detail'),
    path('records/add/', views.record_create, name='record_create'),
    path('records/<int:pk>/delete/', views.record_delete, name='record_delete'),
]
router = DefaultRouter()
router.register(r'cameras', CameraViewSet)
router.register(r'camerarecords', CameraRecordViewSet)

urlpatterns = router.urls