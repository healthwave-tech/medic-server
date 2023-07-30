from django.core.exceptions import SuspiciousOperation
from hogwarts import settings
import jwt

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # make username lowercase
        username = payload['username'].lower()
        payload['username'] = username
        return  payload
    except Exception as e:
        raise SuspiciousOperation("malformed jwt token")
    
def get_image(image_url):
    if settings.USE_S3:
        return image_url
    else:
        return "http://localhost:8000"  + image_url