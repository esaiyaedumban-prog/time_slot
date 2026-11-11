from django.db import models

class Timeslot(models.Model):
    Day = models.CharField(max_length=30)
    startTime = models.TimeField()
    EndTime = models.TimeField()
    subjectname = models.CharField(max_length=100)
    facultyname = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)

    def __str__(self):
        return self.subjectname
