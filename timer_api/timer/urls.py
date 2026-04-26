from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimerPresetViewSet, MeasurementHistoryViewSet

# Router automaticky vygeneruje adresy pro naše views
router = DefaultRouter()
router.register(r'presets', TimerPresetViewSet)
router.register(r'history', MeasurementHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]