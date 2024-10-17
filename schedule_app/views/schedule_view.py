from rest_framework import viewsets, permissions
from ..models.schedule import WeeklySchedule
from ..serializers.schedule_serializer import WeeklyScheduleSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class WeeklyScheduleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing weekly schedules.
    """
    queryset = WeeklySchedule.objects.all()
    serializer_class = WeeklyScheduleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
