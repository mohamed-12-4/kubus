from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField()

class Schedule(models.Model):
    students = models.ManyToManyField(User, related_name="students", blank=True)
    semester = models.CharField(max_length=25)
    day = models.CharField(max_length=50)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    starting_point = models.CharField(max_length=50)
    arriving_point = models.CharField(max_length=50)

    class Meta:
        ordering = ['starting_point', 'arriving_point', 'departure_time']

class Attendance(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
class Points(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()

    

