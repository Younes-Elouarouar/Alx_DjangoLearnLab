
from django.db import models
from django.contrib.auth.models import AbstractUser
"bio", "profile_picture", "models.ImageField", "models.TextField"
class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

