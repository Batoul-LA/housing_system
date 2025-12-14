from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import QRViewSet, AccessLogViewSet

urlpatterns = [
    path('', views.index, name='access-home'),
    path('qr/<int:qr_id>/', views.generate_qr, name='generate_qr'),
    path('scan/', views.scan_qr, name='scan_qr'),
    path('logs/', views.access_log_list, name='access_log_list'),

]
router = DefaultRouter()
router.register(r'qrs', QRViewSet)
router.register(r'accesslogs', AccessLogViewSet)

urlpatterns = router.urls