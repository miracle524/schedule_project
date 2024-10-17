# schedule_app/tests/test_models.py

from django.test import TestCase
from ..models import TimeInterval, DaySchedule, WeeklySchedule

class TimeIntervalModelTest(TestCase):
    def test_create_time_interval(self):
        interval = TimeInterval.objects.create(start="00:00:00", stop="01:00:00", ids=[1, 2])
        self.assertEqual(interval.start, "00:00:00")
        self.assertEqual(interval.stop, "01:00:00")
        self.assertEqual(interval.ids, [1, 2])

class DayScheduleModelTest(TestCase):
    def test_create_day_schedule(self):
        interval = TimeInterval.objects.create(start="00:00:00", stop="01:00:00", ids=[1, 2])
        day_schedule = DaySchedule.objects.create(day="monday")
        day_schedule.intervals.add(interval)
        self.assertEqual(day_schedule.day, "monday")
        self.assertIn(interval, day_schedule.intervals.all())

class WeeklyScheduleModelTest(TestCase):
    def test_create_weekly_schedule(self):
        interval = TimeInterval.objects.create(start="00:00:00", stop="01:00:00", ids=[1, 2])
        day_schedule = DaySchedule.objects.create(day="monday")
        day_schedule.intervals.add(interval)
        weekly_schedule = WeeklySchedule.objects.create(schedule_name="Test Schedule")
        weekly_schedule.days.add(day_schedule)
        self.assertEqual(weekly_schedule.schedule_name, "Test Schedule")
        self.assertIn(day_schedule, weekly_schedule.days.all())
