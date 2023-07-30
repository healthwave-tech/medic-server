from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import jwt
import datetime
from hogwarts import settings


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True)
    dob = models.DateTimeField(null=True)   
    gender = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to="profile/", default=None, null=True, blank=True)

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.datetime.now() + datetime.timedelta(days=60)

        token = jwt.encode({
            'id': self.user.pk,
            'name' : f"{self.user.first_name} {self.user.last_name}",
            'username' : f"{self.user.username}",
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')


        return token
    