from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Organisation(models.Model):
    name = models.TextField()
    practice_num = models.TextField()



class Team(models.Model):
    name = models.TextField()
    Organisation = models.ForeignKey(Organisation, related_name='teams', on_delete=models.CASCADE)


class Member(models.Model):
    user = models.ForeignKey(User, related_name='member_in', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)

    joined = models.DateTimeField(auto_now_add=True)