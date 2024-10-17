from django.db import models

class TimeInterval(models.Model):
    start = models.TimeField()
    stop = models.TimeField()
    ids = models.JSONField()

    def __str__(self):
        return f"{self.start} - {self.stop}"

class DaySchedule(models.Model):
    day = models.CharField(max_length=10)
    intervals = models.ManyToManyField(TimeInterval)

    def __str__(self):
        return self.day

class WeeklySchedule(models.Model):
    schedule = models.ManyToManyField(DaySchedule)

    def __str__(self):
        return "Weekly Schedule"
