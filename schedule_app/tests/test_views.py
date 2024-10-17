# schedule_app/tests/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import WeeklySchedule

class WeeklyScheduleViewSetTest(APITestCase):
    def setUp(self):
        self.url = reverse('weeklyschedule-list')
        self.valid_data = {
            "schedule_name": "Test Schedule",
            "days": [
                {
                    "day": "monday",
                    "intervals": [{"start": "00:00:00", "stop": "01:00:00", "ids": [1, 2]}]
                }
            ]
        }

    def test_create_weekly_schedule(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WeeklySchedule.objects.count(), 1)

    def test_list_weekly_schedules(self):
        WeeklySchedule.objects.create(schedule_name="Sample Schedule")
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_weekly_schedule(self):
        schedule = WeeklySchedule.objects.create(schedule_name="Sample Schedule")
        detail_url = reverse('weeklyschedule-detail', kwargs={'pk': schedule.pk})
        response = self.client.get(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['schedule_name'], "Sample Schedule")
