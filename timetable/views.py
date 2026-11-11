from django.shortcuts import render
from .models import Timeslot
def timetable(request):
    records=Timeslot.objects.all().order_by('Day','startTime')
    return render (request,'timetable.html',{'records':records})
