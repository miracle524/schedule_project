# schedule_app/tests/test_serializers.py

from django.test import TestCase
from ..serializers import TimeIntervalSerializer, DayScheduleSerializer, WeeklyScheduleSerializer
from ..models import TimeInterval, DaySchedule, WeeklySchedule

class TimeIntervalSerializerTest(TestCase):
    def test_serializer_with_valid_data(self):
        data = {"start": "00:00:00", "stop": "01:00:00", "ids": [1, 2]}
        serializer = TimeIntervalSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        data = {"start": "00:00:00", "stop": "invalid_time", "ids": [1, 2]}
        serializer = TimeIntervalSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("stop", serializer.errors)

class DayScheduleSerializerTest(TestCase):
    def test_serializer_with_nested_intervals(self):
        interval_data = {"start": "00:00:00", "stop": "01:00:00", "ids": [1, 2]}
        data = {"day": "monday", "intervals": [interval_data]}
        serializer = DayScheduleSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["day"], "monday")

class WeeklyScheduleSerializerTest(TestCase):
    def test_serializer_with_nested_schedules(self):
        interval_data = {"start": "00:00:00", "stop": "01:00:00", "ids": [1, 2]}
        day_data = {"day": "monday", "intervals": [interval_data]}
        data = {"schedule_name": "Test Schedule", "days": [day_data]}
        serializer = WeeklyScheduleSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["schedule_name"], "Test Schedule")
