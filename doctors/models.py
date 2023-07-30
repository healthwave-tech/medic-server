from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(User, related_name='doctorProfile', on_delete=models.CASCADE)
    qualification = models.TextField()
    occupation = models.TextField()

class Rating(models.Model):
    user = models.ForeignKey(Doctor, related_name='ratings', on_delete=models.CASCADE)
    rating = models.FloatField()

class Practice(models.Model):
    user = models.ForeignKey(Doctor, related_name='practices', on_delete=models.CASCADE)
    location = models.TextField()