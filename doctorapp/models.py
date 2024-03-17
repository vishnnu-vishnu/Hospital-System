from django.db import models
from backend.models import doctordb
from django.utils import timezone

class DoctorAttendance(models.Model):
    doctor = models.ForeignKey(doctordb, on_delete=models.CASCADE)
    punch_in_time = models.DateTimeField(default=timezone.now)
    punch_out_time = models.DateTimeField(null=True, blank=True)

class applyleavedb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    fromdate=models.DateField(max_length=100,null=True,blank=True)
    todate=models.DateField(max_length=100,null=True,blank=True)
    leave=models.CharField(max_length=100,null=True,blank=True)
    reason=models.CharField(max_length=200,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True,default='Pending')


