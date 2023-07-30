from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor

# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField()