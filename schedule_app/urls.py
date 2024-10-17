from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.schedule_view import WeeklyScheduleViewSet, create_user_view

router = DefaultRouter()
router.register(r'schedules', WeeklyScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-user/', create_user_view, name='create_user'),
]
