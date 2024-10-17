from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.schedule_view import WeeklyScheduleViewSet

router = DefaultRouter()
router.register(r'schedules', WeeklyScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
