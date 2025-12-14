from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, BookingViewSet, PaymentViewSet

urlpatterns = [
    path('', views.index, name='booking-home'),
    path('create/', views.create_booking, name='create_booking'),
    path('list/', views.booking_list, name='booking_list'),
    path('payment/<int:booking_id>/', views.add_payment, name='add_payment'),
    path('success/', views.booking_success, name='booking_success')

]

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls
