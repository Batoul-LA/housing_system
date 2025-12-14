from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import WellnessCheckViewSet

urlpatterns = [
    path('', views.index, name='wellness-home'),
     path('add/', views.add_wellness_check, name='add_wellness_check'),
    path('list/', views.wellness_list, name='wellness_list'),
]
router = DefaultRouter()
router.register(r'wellnesschecks', WellnessCheckViewSet)

urlpatterns = router.urls