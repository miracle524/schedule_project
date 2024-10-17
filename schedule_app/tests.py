from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models.schedule import WeeklySchedule
from django.contrib.auth.models import User

class WeeklyScheduleAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('weeklyschedule-list')

    def test_create_weekly_schedule(self):
        data = {
            "schedule": [
                {
                    "day": "monday",
                    "intervals": [
                        {
                            "start": "08:00",
                            "stop": "10:00",
                            "ids": [1, 2, 3]
                        }
                    ]
                }
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(WeeklySchedule.objects.count(), 1)

    def test_get_weekly_schedule(self):
        self.test_create_weekly_schedule()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
