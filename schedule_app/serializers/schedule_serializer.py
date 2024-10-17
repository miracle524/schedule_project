from rest_framework import serializers
from ..models.schedule import TimeInterval, DaySchedule, WeeklySchedule

class TimeIntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInterval
        fields = ['id', 'start', 'stop', 'ids']

class DayScheduleSerializer(serializers.ModelSerializer):
    intervals = TimeIntervalSerializer(many=True)

    class Meta:
        model = DaySchedule
        fields = ['id', 'day', 'intervals']

    def create(self, validated_data):
        intervals_data = validated_data.pop('intervals')
        day_schedule = DaySchedule.objects.create(day=validated_data['day'])
        for interval_data in intervals_data:
            interval = TimeInterval.objects.create(**interval_data)
            day_schedule.intervals.add(interval)
        return day_schedule

class WeeklyScheduleSerializer(serializers.ModelSerializer):
    schedule = DayScheduleSerializer(many=True)

    class Meta:
        model = WeeklySchedule
        fields = ['id', 'schedule']

    def create(self, validated_data):
        schedule_data = validated_data.pop('schedule')
        weekly_schedule = WeeklySchedule.objects.create()
        for day_data in schedule_data:
            intervals_data = day_data.pop('intervals')
            day_schedule = DaySchedule.objects.create(day=day_data['day'])
            for interval_data in intervals_data:
                interval = TimeInterval.objects.create(**interval_data)
                day_schedule.intervals.add(interval)
            weekly_schedule.schedule.add(day_schedule)
        return weekly_schedule
