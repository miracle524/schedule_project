from rest_framework import viewsets, permissions
from ..models.schedule import WeeklySchedule
from ..serializers.schedule_serializer import WeeklyScheduleSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

class WeeklyScheduleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing weekly schedules.
    """
    queryset = WeeklySchedule.objects.all()
    serializer_class = WeeklyScheduleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
@require_POST
def create_user_view(request):
    try:
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password = data['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'success': f'User {username} created successfully.'}, status=201)
    except KeyError:
        return JsonResponse({'error': 'Missing parameters.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
